import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:openqrunb/wikiversity/groupDetail.dart';
import 'package:openqrunb/wikiversity/listInfo.dart';
import './qrcode/scanner.dart';
import './wikiversity/wikiversity.dart';
import './splashScreen.dart';
import './utills.dart';
import 'wikiversity/test/groupsJson.dart';
import 'package:flutter_svg/flutter_svg.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fruição Cultural Unb',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      routes: {
        '/': (context) => MyHomePage(title: 'Home'),
        '/splashScreen': (context) => SplashScreen(),
        '/scanQrCode': (context) => QrCodeScanner(),
        '/showWikiversity': (context) => ShowWikiversity(ModalRoute.of(context)!
            .settings
            .arguments as wikiversityScreenArguments),
        '/groupDetail': (context) => GroupDetail(
            ModalRoute.of(context)!.settings.arguments as groupScreenArguments),
        '/listInfo': (context) => ListInfo(ModalRoute.of(context)!
            .settings
            .arguments as listInfoScreenArguments),
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({required this.title});
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool loaddingData = false;

  @override
  Widget build(BuildContext context) {
    return loaddingData
        ? SplashScreen()
        : Scaffold(
            appBar: AppBar(
              title: Text(widget.title),
            ),
            body: ListView(
              children: [
                Container(
                  alignment: Alignment.center,
                  padding: EdgeInsets.symmetric(vertical: 25),
                  child: Text(
                    'Fruição Cultural',
                    style: TextStyle(fontSize: 32, fontWeight: FontWeight.w500),
                  ),
                ),
                SvgPicture.asset(
                  'assets/unb.svg',
                  allowDrawingOutsideViewBox: false,
                  width: MediaQuery.of(context).size.width -
                      MediaQuery.of(context).size.width / 10,
                  alignment: Alignment.topCenter,
                ),
              ],
            ),
            floatingActionButton: FloatingActionButton(
              onPressed: () {
                _awaitReturnValueFromQrScan(context);
              },
              tooltip: 'Increment',
              child: Icon(Icons.camera_alt),
            ), // This trailing comma makes auto-formatting nicer for build methods.
          );
  }

  // Função que chama o módulo leitor de qrcode e recebe o dado lido
  void _awaitReturnValueFromQrScan(BuildContext context) async {
    try {
      final result = await Navigator.pushNamed(context, '/scanQrCode');

      if (result == "") {
        return;
      }

      Map<String, dynamic> scandata = jsonDecode(result.toString());

      final qrCodeString = scandata['value'];
      final qrCodeError = scandata['error'];

      final openStreetMapRegex = RegExp(
          r"(http|https):\/\/www\.openstreetmap\.org\/(node|way|relation)\/(\d+)");

      final openSteetMapId =
          openStreetMapRegex.firstMatch(qrCodeString)?.group(3) ?? null;

      final openSteetMapObject =
          openStreetMapRegex.firstMatch(qrCodeString)?.group(2) ?? null;

      if (qrCodeError == 0 && openSteetMapId != null) {
        // OverPass Query
        var queryParameters = {
          'data':
              '<osm-script output="json" output-config=""> <id-query type="$openSteetMapObject" ref="$openSteetMapId"/> <print e="" from="_" geometry="skeleton" ids="yes" limit="" mode="tags" n="" order="id" s="" w=""/> </osm-script>',
        };

        setState(() {
          loaddingData = true;
        });

        final response = await http.get(
          Uri.http('overpass-api.de', '/api/interpreter', queryParameters),
          headers: <String, String>{
            'Content-Type': 'application/json; charset=UTF-8',
          },
        );
        if (response.statusCode == 200) {
          final wikiversityUrl = jsonDecode(response.body)['elements'][0]
                  ?['tags']['wikiversity'] ??
              null;
          if (wikiversityUrl != null) {
            // CHAMADA API com a url
            // RECEBE JSON

            //sleep(Duration(milliseconds: 1000));

            Map<String, dynamic> wikiversityJson = GoupsJson.teste1;

            Navigator.pushNamed(context, '/showWikiversity',
                arguments: wikiversityScreenArguments(wikiversityJson));
            setState(() {
              loaddingData = false;
            });
          } else {
            setState(() {
              loaddingData = false;
            });
            Utils.showErrorDialog(context,
                'Can not find Wikiversity element in the node ${jsonDecode(response.body)['elements'][0]?['tags']['name'] ?? ""}');
          }
        } else {
          setState(() {
            loaddingData = false;
          });
          Utils.showErrorDialog(context,
              "Error quering for this OpenStreetMap Node. Status Code: ${response.statusCode}");
        }
      } else {
        Utils.showErrorDialog(context,
            qrCodeError == 0 ? "Invalid OpenStreetMap Url" : qrCodeString);
      }
    } catch (error) {
      setState(() {
        loaddingData = false;
      });
      Utils.showErrorDialog(context, error.toString());
    }
  }
}
