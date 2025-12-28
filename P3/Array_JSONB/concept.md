# 1. Why JSON in SQL?

Sometimes data doesn't fit neatly into columns.

* **User Settings:** `{ "theme": "dark", "notifications": true }`

* **Product Specs:** `{ "color": "red", "weight": "5kg", "wireless": true }`

Postgres allows you to store this as a `JSONB` column and **query inside it** efficiently.

---

## 2. The Operators

* `->` : Get JSON object field (returns JSON).

* `->>` : Get JSON object field as **Text**. (Use this 99% of the time).

* `@>` : "Contains". Does the JSON on the left contain the JSON on the right?

---

## 3. Example

Row: `info = { "customer": "John", "tags": ["vip", "new"] }`

* `SELECT info ->> 'customer'` Returns `"John"`.

* `WHERE info @> '{"tags": ["vip"]}'` Returns True (The row is a VIP).

---