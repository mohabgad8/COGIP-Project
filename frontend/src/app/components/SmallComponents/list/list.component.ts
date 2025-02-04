import {Component, input, Input} from '@angular/core';
import {NgForOf, NgIf} from '@angular/common';


@Component({
  selector: 'app-list',
  imports: [
    NgForOf,
    NgIf,
  ],
  templateUrl: './list.component.html',
  standalone: true,
  styleUrl: './list.component.css'
})
export class ListComponent {
  @Input() title: string | undefined;
  @Input() column: {key: string, label: string}[] = [];
  @Input() data: any[] = [];

  @Input() showSearchBar: boolean = false;

}
