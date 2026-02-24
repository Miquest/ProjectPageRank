// Helper class for easier JSON handling
class SearchResult {
  final Uri url;
  final String title;
  String? content;
  final DateTime lastCrawl;
  final double pagerankScore;

  SearchResult({
    required this.url,
    required this.title,
    required this.lastCrawl,
    required this.pagerankScore,
    this.content,
  });

  factory SearchResult.fromJson(Map json) {
    return SearchResult(
      url: Uri.parse(json["url"]),
      title: json["title"] ?? "Unknown",
      lastCrawl: DateTime.parse(json["last_crawl"]),
      pagerankScore: json["score"],
      content: json["content"] ?? "",
    );
  }
}
