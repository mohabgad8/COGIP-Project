import { Component } from '@angular/core';
import {SidebarComponent} from '../../SmallComponents/sidebar/sidebar.component';
import {StatisticsComponent} from '../../SmallComponents/statistics/statistics.component';

@Component({
  selector: 'app-dashboardpage',
  imports: [
    SidebarComponent, StatisticsComponent
  ],
  standalone:true,
  templateUrl: './dashboardpage.component.html',
  styleUrl: './dashboardpage.component.css'
})
export class DashboardpageComponent {
}
