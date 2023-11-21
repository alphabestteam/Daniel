import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
  count: number = 5;
  total: number = 0;
  
  @Output() totalChange: EventEmitter<number> = new EventEmitter<number>();


  decrement(): number {
    this.count--;
    this.isOverTen();
    return this.count;
  }

  increment(): number {
    this.count++;
    this.isOverTen();
    return this.count;
  }

  isOverTen(): void {
    if (this.count % 10 === 0 && this.count) {
      this.total += (this.count > 0) ? 10 : -10;
      this.totalChange.emit(this.total);
      this.count = 0;
    }
  }
}
