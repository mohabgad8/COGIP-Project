import {Component} from '@angular/core';
import {RouterLink} from '@angular/router';

interface FormField {
  label: string;
  placeholder: string;
}
@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  standalone: true,
  imports: [
    RouterLink
  ],
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {

contact = [
    {
      id:1, child: { name: "Bertram", lastName: 'Gilfoyle', pdp: 'assets/img/Avatar_one.png' }
    },
    {
      id:2, child: { name: "Henry", lastName: "George", pdp: 'assets/img/Avatar_two.png' }
    }
  ]

}
