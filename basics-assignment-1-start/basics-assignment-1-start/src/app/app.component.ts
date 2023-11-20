import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  displayed = false;

  changeAlert() {
    this.displayed = !this.displayed;
  }
}
