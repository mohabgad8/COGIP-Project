import { Component } from '@angular/core';
import {RouterOutlet} from '@angular/router';
import {HeaderComponent} from './components/SmallComponents/header/header.component';
import {FooterComponent} from './components/SmallComponents/footer/footer.component';
import {PaginationComponent} from './components/SmallComponents/pagination/pagination.component';



@Component({
  selector: 'app-root',
  standalone:true,
  imports: [HeaderComponent, FooterComponent, RouterOutlet, PaginationComponent],
  templateUrl:'app.component.html',
  styleUrl: 'app.component.css'
})
export class AppComponent {


}
