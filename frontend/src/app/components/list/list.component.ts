import { Component, Input } from '@angular/core';
import {NgForOf} from '@angular/common';


@Component({
  selector: 'app-list',
  imports: [
    NgForOf
  ],
  templateUrl: './list.component.html',
  styleUrl: './list.component.css'
})
export class ListComponent {

  @Input() column: {key: string, label: string}[] = [];
  @Input() data: any[] = [];

}
