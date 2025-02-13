import { Component } from '@angular/core';
import {SidebarComponent} from '../../SmallComponents/sidebar/sidebar.component';
import {RouterOutlet} from '@angular/router';



interface FormField {
  label: string
  placeholder: string
}
@Component({
  selector: 'app-dashboardpage',
  imports: [
    SidebarComponent,
    RouterOutlet,
  ],
  standalone:true,
  templateUrl: './dashboardpage.component.html',
  styleUrl: './dashboardpage.component.css'
})
export class DashboardpageComponent {
}
