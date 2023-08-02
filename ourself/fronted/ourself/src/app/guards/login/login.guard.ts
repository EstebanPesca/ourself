import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { UserService } from 'src/app/service/api/user.service';

@Injectable({
  providedIn: 'root',
})

export class loginGuard implements CanActivate{

  constructor (private router: Router, private userService: UserService){}

  canActivate(): boolean{
    if (this.userService.isLogged()){
      return true;
    } else{
      localStorage.clear();
      this.router.navigate(['/login']);
      return false;
    }
  }
}
