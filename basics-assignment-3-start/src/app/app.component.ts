import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  isHidden: boolean = false;
  counter: number = 0;
  textButton: string = 'Show Details';
  arr: number[] = [];

  checkIsHidden() {
    this.textButton = this.isHidden ? 'Show Details' : 'Hide Details';
    this.isHidden = !this.isHidden;
    this.counter++;
    this.arr.push(this.counter);
  }
  isBackgroundBlue(index: number): boolean {
    return index >= 5;
  }
}
