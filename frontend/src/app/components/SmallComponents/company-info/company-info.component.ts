import { Component, Input } from '@angular/core';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-company-info',
  imports: [
    NgForOf
  ],
  templateUrl: './company-info.component.html',
  styleUrl: './company-info.component.css'
})

export class CompanyInfoComponent {

  @Input() contact: {key: string, label: string}[] = [];

}
