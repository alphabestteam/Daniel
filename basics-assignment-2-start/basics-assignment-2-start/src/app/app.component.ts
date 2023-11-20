import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userName: string = '';
  deactive: boolean = false;

   checkEmptyInput() {
    if (this.userName !== '') {
      this.userName = '';
      this.deactive = false;
    } else {
      this.deactive = true;
    }
  }
}
