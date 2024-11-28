import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { LocalStorageService } from './app/local-storage.service'; // Poprawny import

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    LocalStorageService // Rejestracja serwisu w providers
  ]
});
