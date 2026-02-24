import 'dart:convert';

import 'package:http/http.dart' as http;

class SearchClient {
  final String baseUrl = "http://localhost:8000";

  Future<List> searchWithKeyword(String keyword) async {
    Uri uri = Uri.parse(
      "$baseUrl/search/keyword/?search=${keyword.toLowerCase()}",
    );

    final response = await http.get(uri);
    return jsonDecode(response.body);
  }
}
