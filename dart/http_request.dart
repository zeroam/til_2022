import 'package:http/http.dart' as http;
import 'package:http/retry.dart';
import 'dart:convert';

Future<void> normalRequest() async {
  var url = Uri.https('example.com', 'whatsit/create');
  var response =
      await http.post(url, body: {'name': 'doodle', 'color': 'blue'});
  print('Response status: ${response.statusCode}');
  print('Response body: ${response.body}');
  print(await http.read(Uri.https('example.com', 'foobar.txt')));
}

Future<void> clientRequest() async {
  var client = http.Client();
  try {
    var response = await client.post(Uri.https('example.com', 'whatsit/create'),
        body: {'name': 'doodle', 'color': 'blue'});
    var decodedResponse = jsonDecode(utf8.decode(response.bodyBytes)) as Map;
    var uri = Uri.parse(decodedResponse['uri'] as String);
    print(await client.get(uri));
  } finally {
    client.close();
  }
}

Future<void> retryRequest() async {
  final client = RetryClient(http.Client());
  try {
    print(await client.read(Uri.https('example.org', '')));
  } finally {
    client.close();
  }
}

Future<void> main() async {
  // await normalRequest();
  // await clientRequest();
  await retryRequest();
}
