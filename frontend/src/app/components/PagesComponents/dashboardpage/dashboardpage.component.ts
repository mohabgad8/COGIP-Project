import { Component } from '@angular/core';
import {SidebarComponent} from '../../SmallComponents/sidebar/sidebar.component';

@Component({
  selector: 'app-dashboardpage',
  imports: [
    SidebarComponent
  ],
  standalone:true,
  templateUrl: './dashboardpage.component.html',
  styleUrl: './dashboardpage.component.css'
})
export class DashboardpageComponent {
}
