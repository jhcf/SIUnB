import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class listInfoScreenArguments {
  final String type;
  final Map<String, dynamic> listJson;
  listInfoScreenArguments(this.type, this.listJson);
}

class ListInfo extends StatelessWidget {
  final listInfoScreenArguments arguments;
  ListInfo(this.arguments);

  @override
  Widget build(BuildContext context) {
    Map<String, List<dynamic>> infosMap = {
      "Wikidata": arguments.listJson['wikidata'],
      "Wikipedia": arguments.listJson['wikipedia'],
      "Facebook": arguments.listJson['facebook'],
      "Instagram": arguments.listJson['instagram'],
      "Twitter": arguments.listJson['twitter'],
      "Youtube": arguments.listJson['youtube'],
      "Teams": arguments.listJson['teams'],
      "Stream": arguments.listJson['stream'],
      "OpenStretMap": arguments.listJson['osm'],
    };

    final idRegex = RegExp(r"\/(?:.(?!\/))+$");
    final childrenList = <Widget>[
      Container(
        padding: EdgeInsets.all(6),
        child: Text(arguments.listJson['name'],
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
            )),
      ),
      Container(
        padding: EdgeInsets.all(6),
        child: Text(arguments.listJson['description'],
            style: TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.bold,
                color: Colors.grey[500])),
      ),
    ];
    for (var key in infosMap.keys) {
      childrenList.add(
        Card(
          child: Container(
            padding: EdgeInsets.all(6),
            child: Column(
              children: [
                Align(
                    alignment: Alignment.centerLeft,
                    child: Text(
                      ' ${arguments.type}s ${key}: ',
                      style: TextStyle(fontSize: 20),
                    )),
                infosMap[key]?.isNotEmpty ?? false
                    ? ListView.builder(
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        itemCount: infosMap[key]?.length,
                        itemBuilder: (BuildContext context, int index) {
                          return Container(
                            child: InkWell(
                                child: Row(
                                  children: [
                                    Icon(
                                      Icons.subdirectory_arrow_right_rounded,
                                      color: Colors.grey[500],
                                    ),
                                    Expanded(
                                      child: Text(
                                        '${key}${Uri.decodeFull(idRegex.firstMatch(infosMap[key]?[index])?.group(0) ?? '')}',
                                        style: TextStyle(
                                            fontSize: 16,
                                            color:
                                                Theme.of(context).primaryColor),
                                        overflow: TextOverflow.fade,
                                      ),
                                    ),
                                  ],
                                ),
                                onTap: () => launch(infosMap[key]?[index])),
                            margin: EdgeInsets.symmetric(
                                vertical: 2, horizontal: 6),
                          );
                        },
                      )
                    : Align(
                        alignment: Alignment.centerLeft,
                        child: Container(
                          padding: EdgeInsets.all(6),
                          child: Text(
                            'No items',
                            style: TextStyle(
                              color: Colors.red,
                            ),
                          ),
                        )),
              ],
            ),
          ),
        ),
      );
    }

    return Scaffold(
        appBar: AppBar(
          title: Text(this.arguments.type),
        ),
        body: Container(
          child: ListView(
              shrinkWrap: true,
              padding: EdgeInsets.all(15.0),
              children: childrenList),
        ));
  }
}
