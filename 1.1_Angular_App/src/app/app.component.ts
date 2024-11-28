import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CarsComponent } from "./cars/cars.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CarsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = '1.1_Angular_App';
}