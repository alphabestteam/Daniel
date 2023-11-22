import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  count: number = 0;
  options: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  isWarningAlert: boolean = false;

  getRange(count: number): Number[] {
    return Array(count);
  }

  changeAlert() {
    this.isWarningAlert = !this.isWarningAlert;
  }
}
