### Link
- [chap02. Repository](https://github.com/cosmicpython/code/tree/chapter_02_repository)
- [chap02. Repository Exercise](https://github.com/cosmicpython/code/tree/chapter_02_repository_exercise)

```mermaid
classDiagram
	direction LR
	class Batch {
		int reference
		str sku
		date eta
		int _purchased_quantity
		OrderLine _allocations
	}

	class OrderLine {
		str orderid
		str sku
		int qty
	}

	Batch *-- OrderLine
```