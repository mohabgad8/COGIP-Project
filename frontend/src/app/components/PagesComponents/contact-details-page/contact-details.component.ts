import { Component } from '@angular/core';
import {ContactInfoComponent} from '../../SmallComponents/contact-info/contact-info.component';

@Component({
  selector: 'app-contact-details',
  imports: [
    ContactInfoComponent
  ],
  templateUrl: './contact-details.component.html',
  styleUrl: './contact-details.component.css'
})
export class ContactDetailsComponent {

}
