import { Component } from '@angular/core';
import {HeaderComponent} from './components/header/header.component';
import {BannerComponent} from './components/banner/banner.component';
import {FooterComponent} from './components/footer/footer.component';


@Component({
  selector: 'app-root',
  standalone:true,
  imports:[HeaderComponent, BannerComponent, FooterComponent],
  templateUrl:'app.component.html',
  styleUrl: 'app.component.css'
})
export class AppComponent {

}
