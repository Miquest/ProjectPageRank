import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/internal/search_client.dart';
import 'package:frontend/results/results.dart';

class Search extends StatefulWidget {
  const Search({super.key});

  @override
  State<Search> createState() => _SearchState();
}

class _SearchState extends State<Search> {
  SearchClient client = SearchClient();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(15),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SvgPicture.asset("assets/search_person.svg", height: 200),

              SizedBox(height: 20),

              Text(
                "Searchy",
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 50),
              ),

              SizedBox(height: 20),

              ConstrainedBox(
                constraints: BoxConstraints(maxWidth: 500),
                child: SearchBar(
                  leading: Icon(Icons.search),
                  hintText: "Search something...",
                  onSubmitted: (keyword) {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => Results(keyword: keyword),
                      ),
                    );
                  },
                  padding: WidgetStatePropertyAll(
                    EdgeInsets.fromLTRB(20, 10, 20, 10),
                  ),
                ),
              ),

              SizedBox(height: 30),
              TextButton(
                onPressed: () => showLicensePage(context: context),
                child: Text("Licenses"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
