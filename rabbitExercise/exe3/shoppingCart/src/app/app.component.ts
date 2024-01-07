import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ShoppingCartComponent } from "./shopping-cart/shopping-cart.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
    imports: [CommonModule, RouterOutlet, ShoppingCartComponent]
})
export class AppComponent {
  title = 'shoppingCart';
}
