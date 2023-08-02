import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './views/login/login.component';
import { HomeComponent } from './views/home/home.component';
import { SidebarComponent } from './templates/sidebar/sidebar.component';
import { loginGuard } from './guards/login/login.guard';
import { LayoutComponent } from './templates/layout/layout.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    canActivate: [loginGuard],
    children: [
      {path:'', redirectTo: 'home', pathMatch:'full'},
      {path: 'home', component: HomeComponent},
    ]
  },
  {path:'login', component:LoginComponent},
  {path:'**' , redirectTo:'login', pathMatch:'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

// Exporting the components
export const routingComponents = [LoginComponent, HomeComponent, SidebarComponent, LayoutComponent,SidebarComponent]
