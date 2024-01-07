import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-shopping-cart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.scss']
})
export class ShoppingCartComponent implements OnInit {

  list: string[] = ['Shirt', 'Pants', 'Shoes', 'Hat', 'Sunglasses', 'Bag', 'Watch', 'Jacket'];
  storedList: string[] = [];
  shoppingList: string[] = [];
  showShoppingLIst:boolean =false;

  constructor() {}

  ngOnInit(): void {
    localStorage.setItem('storedList', JSON.stringify(this.list));

    const storedListString = localStorage.getItem('storedList');

    if (storedListString) {
      this.storedList = JSON.parse(storedListString);
    }
  }

  addToCart(item: string): void {
    this.shoppingList.push(item);
    localStorage.setItem('shoppingList', JSON.stringify(this.shoppingList));
    alert('Added item successfully!')

  }
  processToPayment(): void {
    this.showShoppingLIst = true;
  }
}
