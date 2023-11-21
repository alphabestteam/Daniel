import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';


import { AppComponent } from './app.component';
import { MyOuterComponent } from './my-outer/my-outer.component';
import { MyInnerComponent } from './my-inner/my-inner.component';

@NgModule({
  declarations: [
    AppComponent,
    MyOuterComponent,
    MyInnerComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
