import { Component, Input, OnInit} from '@angular/core';
import {NgForOf, NgIf} from '@angular/common';


@Component({
  selector: 'app-details',
  imports: [
    NgForOf,
    NgIf,

  ],
  templateUrl: './details.component.html',
  standalone: true,
  styleUrl: './details.component.css'
})

export class DetailsComponent{

  @Input() contact: { key: string, label: string }[] = []
  @Input() companyData: any = null;
  @Input() showdata: boolean= true;
  @Input() contactData: any = null;


  get companycategories() {
    return this.companyData
    ? Object.keys(this.companyData).map(key => ({
        key: key,
        label: key.charAt(0).toUpperCase() + key.slice(1)
      }))
      :[];
  }

    get contactcategories() {
      return this.contactData
        ? Object.keys(this.contactData).map(key => ({
          key: key,
          label: key.charAt(0).toUpperCase() + key.slice(1)
        }))
        : [];
    }
}


