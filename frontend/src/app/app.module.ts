import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { API_AUDIENCE, AUTH0_DOMAIN, CLIENTID } from './env';
import { AuthModule } from '@auth0/auth0-angular';
import { HomeComponent } from './pages/home/home.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { JobSearchFormComponent } from './components/content/job-search-form/job-search-form.component';
import { JobCardComponent } from './components/content/job-card/job-card.component';
import { AppRoutingModule } from './app-routing.module';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DashboardComponent,
    HeaderComponent,
    FooterComponent,
    SidebarComponent,
    JobSearchFormComponent,
    JobCardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    HttpClientModule,
    BrowserModule,
    HttpClientModule,
    AuthModule.forRoot({
      domain: AUTH0_DOMAIN,
      clientId: CLIENTID,
      audience: API_AUDIENCE,
      redirectUri: window.location.origin,
    }),
  ],
  providers: [
    {
      provide: Window,
      useValue: window,
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
