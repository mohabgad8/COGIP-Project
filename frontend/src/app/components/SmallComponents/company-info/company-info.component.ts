import { Component, Input } from '@angular/core';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-company-info',
  imports: [
    NgForOf,
  ],
  templateUrl: './company-info.component.html',
  standalone: true,
  styleUrl: './company-info.component.css'
})

export class CompanyInfoComponent {

  @Input() contact: { key: string, label: string }[] = [];
}
