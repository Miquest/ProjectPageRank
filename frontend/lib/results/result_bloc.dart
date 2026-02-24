import 'package:flutter/material.dart';
import 'package:frontend/internal/search_client.dart';
import 'package:frontend/internal/search_result.dart';

class ResultBloc with ChangeNotifier {
  SearchClient client = SearchClient();
  bool loading = true;
  List<SearchResult> results = [];

  Future<void> searchWithKeyword(String keyword) async {
    List jsonResults = await client.searchWithKeyword(keyword);
    results = jsonResults.map((x) => SearchResult.fromJson(x)).toList();
    loading = false;
    notifyListeners();
  }
}
