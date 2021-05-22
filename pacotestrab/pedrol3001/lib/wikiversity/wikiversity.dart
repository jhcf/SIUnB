import 'package:flutter/material.dart';
import 'package:openqrunb/wikiversity/groupDetail.dart';

class wikiversityScreenArguments {
  final Map<String, dynamic> wikiJson;
  wikiversityScreenArguments(this.wikiJson);
}

class ShowWikiversity extends StatefulWidget {
  ShowWikiversity(this.arguments);
  final wikiversityScreenArguments arguments;

  @override
  State<StatefulWidget> createState() => _ShowWikiversityState();
}

class _ShowWikiversityState extends State<ShowWikiversity> {
  @override
  Widget build(BuildContext context) {
    List<dynamic> jsonGroups = widget.arguments.wikiJson['groups'];
    return Scaffold(
      appBar: AppBar(
        title: Text('Grupos Wikiversity'),
      ),
      body: ListView.separated(
        
          padding: const EdgeInsets.all(8),
          itemCount: jsonGroups.length,
          separatorBuilder: (BuildContext context, int index) =>
              const Divider(),
          itemBuilder: (BuildContext context, int index) {
            return TextButton(
              style: TextButton.styleFrom(
                alignment: Alignment.centerLeft,
                padding: EdgeInsets.symmetric(vertical: 20, horizontal: 10),
                backgroundColor: Colors.grey[200],
                shadowColor: Colors.black,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(5))),
              ),
              onPressed: () => {
                Navigator.pushNamed(context, '/groupDetail',
                    arguments: groupScreenArguments(jsonGroups[index]))
              },
              child: Expanded(
                child: Row(
                  children: [
                    Flexible(
                      flex: 6,
                      child: Container(
                          alignment: Alignment.centerLeft,
                          child: Text(jsonGroups[index]['name'])),
                    ),
                    Expanded(flex: 1, child: Icon(Icons.chevron_right_rounded))
                  ],
                ),
              ),
            );
          }),
    );
  }
}
