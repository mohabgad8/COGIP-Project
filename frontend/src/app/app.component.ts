import { Component } from '@angular/core';
import {HeaderComponent} from './components/header/header.component';
import {BannerComponent} from './components/banner/banner.component';


@Component({
  selector: 'app-root',
  standalone:true,
  imports:[HeaderComponent, BannerComponent],
  templateUrl:'app.component.html',
  styleUrl: 'app.component.css'
})
export class AppComponent {

}
