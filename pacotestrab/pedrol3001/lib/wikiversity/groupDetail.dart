import 'package:flutter/material.dart';

import 'listInfo.dart';

class groupScreenArguments {
  final Map<String, dynamic> groupJson;
  groupScreenArguments(this.groupJson);
}

class GroupDetail extends StatefulWidget {
  GroupDetail(this.arguments);
  final groupScreenArguments arguments;

  @override
  State<StatefulWidget> createState() => _GroupDetailState();
}

class _GroupDetailState extends State<GroupDetail> {
  @override
  Widget build(BuildContext context) {
    Map<String, dynamic> groupJson = widget.arguments.groupJson;

    Map<String, List<dynamic>> groupMaps = {
      "Eventos": groupJson['events'],
      "Serviços": groupJson['services'],
      "Assets": groupJson['assets'],
    };

    final childrenGroups = <Widget>[];

    for (var key in groupMaps.keys) {
      childrenGroups.add(
        groupMaps[key]?.isNotEmpty ?? false
            ? Container(
                padding: EdgeInsets.all(20),
                child: DropdownButton<dynamic>(
                  icon: Icon(Icons.arrow_drop_down_sharp),
                  iconSize: 30,
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                  isExpanded: true,
                  hint: Text(key),
                  items: (groupMaps[key]
                      ?.asMap()
                      .map((i, value) {
                        return MapEntry(
                            i,
                            DropdownMenuItem<dynamic>(
                              value: i,
                              child: new Text(value['name'],
                                  style: TextStyle(
                                      fontSize: 15,
                                      fontWeight: FontWeight.normal,
                                      color: Theme.of(context).primaryColor)),
                            ));
                      })
                      .values
                      .toList()),
                  onChanged: (i) => {
                    Navigator.pushNamed(context, '/listInfo',
                        arguments:
                            listInfoScreenArguments(key, groupMaps[key]?[i]))
                  },
                ),
              )
            : SizedBox(),
      );
    }

    return Scaffold(
        appBar: AppBar(
          title: Text('Grupo'),
        ),
        body: Container(
          padding: EdgeInsets.all(8),
          child: ListView(
            children: [
              SizedBox(
                height: 20,
              ),
              Align(
                alignment: Alignment.centerLeft,
                child: Text(
                  'Nome: ${groupJson['name']}',
                  style: TextStyle(fontSize: 20),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Align(
                alignment: Alignment.centerLeft,
                child: Text(
                  'Descrição: ${groupJson['description']}',
                  style: TextStyle(fontSize: 15, color: Colors.grey[600]),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Card(
                child: Column(
                  children: childrenGroups,
                ),
              ),
            ],
          ),
        ));
  }
}
