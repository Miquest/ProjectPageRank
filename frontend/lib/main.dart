import 'package:flutter/material.dart';
import 'package:frontend/search.dart';

void main() {
  runApp(const Searchy());
}

class Searchy extends StatelessWidget {
  const Searchy({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      themeMode: ThemeMode.dark,
      theme: ThemeData(
        colorScheme: .fromSeed(
          seedColor: Colors.deepPurple,
          brightness: Brightness.dark,
        ),
      ),
      home: const Search(),
    );
  }
}
