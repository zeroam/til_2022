Future<String> fetchUserOrder() {
  return Future.delayed(Duration(seconds: 2), () => 'Large Latte');
}

void main() async {
  String order = await fetchUserOrder();
  print(order);
}
