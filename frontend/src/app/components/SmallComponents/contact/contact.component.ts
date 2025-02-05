import { Component, Input } from '@angular/core';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-contact',
  imports: [
    NgForOf
  ],
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.css'
})

export class ContactComponent {

  @Input() contact: {key: string, label: string}[] = [];

}
