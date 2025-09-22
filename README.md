# E-Commerce Mock Platform

## Project Overview

## Features

## Tech Stack
## Data Model

| Table       | Fields                                                          |
|-------------|-----------------------------------------------------------------|
| users       | id; email; password_hash; created_at                            |
| products    | id; name; description; price; image_url; created_at             |
| carts       | id; user_id; created_at                                         |
| cart_items  | id; cart_id; product_id; quantity                               |
| orders      | id; user_id; total_amount; status; created_at                   |
| order_items | id; order_id; product_id; quantity; price_at_purchase           |


## Folder Structure

## Setup & Run
