import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css']
})

  export class MyOuterComponent {
    parentTotal: number = 0;
  
    handleTotalChange(updatedTotal: number): void {
      this.parentTotal = updatedTotal;
    }
  }
  