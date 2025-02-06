import { Component } from '@angular/core';
import {NgForOf, NgOptimizedImage} from '@angular/common';

// @ts-ignore
@Component({
  selector: 'app-contact-people',
  imports: [
    NgForOf,
    NgOptimizedImage
  ],
  templateUrl: './contact-people.component.html',
  styleUrl: './contact-people.component.css'
})
export class ContactPeopleComponent {

  title = 'Contact People';

  contact = [
    {
      id:1, child: { name: "Bertram", lastName: 'Gilfoyle', pdp: 'assets/img/Avatar_one.png' }
    },
    {
      id:2, child: { name: "Henry", lastName: "George", pdp: 'assets/img/Avatar_two.png' }
    }
  ]
}
