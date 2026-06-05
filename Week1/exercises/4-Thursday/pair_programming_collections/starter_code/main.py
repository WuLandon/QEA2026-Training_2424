"""
Main Program — Product Inventory System
Week 1, Thursday | Pair Programming Exercise

Wire everything together here. Complete each numbered section.
Run with:  python main.py

References:
    written/4-Thursday/lists.md
    written/4-Thursday/tuples.md
    written/4-Thursday/sets.md
    written/4-Thursday/exception-handling-custom-exceptions.md
    written/4-Thursday/try-except.md
"""

from exceptions import InsufficientStockError, ProductNotFoundError
from inventory import Inventory
from product import Product


def section(title: str) -> None:
    print(f"\n{'─' * 55}")
    print(f"  {title}")
    print(f"{'─' * 55}")


def main():
    inv = Inventory()

    # ── 1. Add at least 8 products across 3+ categories ───────────────────
    section("1. Loading Inventory")

    products = [
        Product("Laptop Pro", 1299.99, stock=10, category="electronics"),
        Product("Mechanical Keyboard", 119.99, stock=25, category="accessories"),
        Product("Wireless Mouse", 49.99, stock=40, category="accessories"),
        Product("4K Monitor", 349.99, stock=12, category="electronics"),
        Product("USB-C Hub", 34.99, stock=30, category="accessories"),
        Product("Project Management Suite", 199.99, stock=50, category="software"),
        Product("Antivirus Plus", 59.99, stock=60, category="software"),
        Product("Gaming Headset", 89.99, stock=18, category="electronics"),
    ]

    for product in products:
        product_id = inv.add_product(product)
        print(f"  Added: {product} -> ID={product_id}")

    # ── 2. Display all products sorted by price ────────────────────────────
    section("2. All Products (sorted by price)")

    for product in sorted(inv.products.values()):
        print(f"  {product}")

    # ── 3. Search products by keyword ─────────────────────────────────────
    section("3. Search: 'pro'")

    for product in inv.search("pro"):
        print(f"  {product}")

    # ── 4. Filter by category ─────────────────────────────────────────────
    section("4. Category: 'electronics'")

    for product in inv.by_category("electronics"):
        print(f"  {product}")

    # ── 5. Sell products — one should succeed, one should fail ────────────
    section("5. Sell Operations")

    inv.sell(1, 2)
    print(f"  Sold 2 units of {inv.get_product(1).name}")

    try:
        inv.sell(4, 20)
    except InsufficientStockError as e:
        print(f"  {e}")
        print(f"  Requested: {e.requested}, Available: {e.available}")

    # ── 6. Access a non-existent product ID ───────────────────────────────
    section("6. Non-Existent Product Lookup")

    try:
        inv.get_product(9999)
    except ProductNotFoundError as e:
        print(f"  {e}")

    # ── 7. Transaction history ────────────────────────────────────────────
    section("7. Recent Transaction History")

    for e in inv.history:
        print(f"  {e}")

    # ── 8. Inventory summary ──────────────────────────────────────────────
    section("8. Inventory Summary")

    for key, value in inv.summary().items():
        print(f"  {key}: {value}")

    # ── 9. Set operations on categories ───────────────────────────────────
    section("9. Set Operations on Categories")

    my_wishlist = {"electronics", "gaming", "software"}

    print(f"  Union: {inv.categories | my_wishlist}")
    print(f"  Intersection: {inv.categories & my_wishlist}")
    print(f"  Difference: {my_wishlist - inv.categories}")

    # ── 10. Tuple-based product configurations ────────────────────────────
    section("10. Product Configs as Tuples")

    configs = [
        ("Webcam", 79.99, 14, "electronics"),
        ("Desk Mat", 19.99, 35, "accessories"),
        ("Photo Editor", 149.99, 20, "software"),
    ]

    for name, price, stock, category in configs:
        inv.add_product(Product(name, price, stock=stock, category=category))

    print(f"  Total products in inventory: {len(inv)}")


if __name__ == "__main__":
    main()
