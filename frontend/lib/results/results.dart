import 'package:flutter/material.dart';
import 'package:frontend/internal/search_result.dart';
import 'package:frontend/results/result_bloc.dart';
import 'package:url_launcher/url_launcher.dart';

class Results extends StatefulWidget {
  final String keyword;

  const Results({super.key, required this.keyword});

  @override
  State<Results> createState() => _ResultsState();
}

class _ResultsState extends State<Results> {
  ResultBloc bloc = ResultBloc();

  @override
  Widget build(BuildContext context) {
    bloc.searchWithKeyword(widget.keyword);

    return Scaffold(
      appBar: AppBar(),
      body: Padding(
        padding: const EdgeInsets.all(15),
        child: ListenableBuilder(
          listenable: bloc,
          builder: (BuildContext context, Widget? child) {
            return ListView(
              children: [
                SizedBox(height: 30),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  spacing: 20,
                  children: [
                    Icon(Icons.search, size: 30),
                    Text(
                      widget.keyword,
                      style: TextStyle(
                        fontSize: 30,
                        fontWeight: FontWeight.w700,
                        fontStyle: FontStyle.italic,
                      ),
                    ),
                  ],
                ),

                SizedBox(height: 20),
                Divider(indent: 30, endIndent: 30),
                SizedBox(height: 20),

                if (bloc.loading)
                  SizedBox(height: 20, child: CircularProgressIndicator()),

                ...[
                  for (SearchResult result in bloc.results)
                    ListTile(
                      title: Text(result.title),
                      subtitle: Text(result.content ?? ""),
                      trailing: Icon(Icons.arrow_forward_ios_sharp),
                      onTap: () async {
                        await launchUrl(result.url);
                      },
                    ),
                ],
              ],
            );
          },
        ),
      ),
    );
  }
}
