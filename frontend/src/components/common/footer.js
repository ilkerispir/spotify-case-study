import React from 'react';

import { BackTop } from 'antd';

function AppFooter() {
  return (
    <div className="container-fluid">
      <div className="footer">
        <ul className="socials">
          <li className="facebook"><a href="https://www.facebook.com/alotechbulutsantral"><i className="fab fa-facebook-f"></i></a></li>
          <li className="twitter"><a href="https://www.twitter.com/alo_tech"><i className="fab fa-twitter"></i></a></li>
          <li className="instagram"><a href="https://www.instagram.com/alotechbulut"><i className="fab fa-instagram"></i></a></li>
          <li className="linkedin"><a href="https://www.linkedin.com/company/alotechbulut/"><i className="fab fa-linkedin-in"></i></a></li>
          <li className="youtube"><a href="https://www.youtube.com/channel/UCVwWKr-vTnxXdGd1A3BhqWA"><i className="fab fa-youtube"></i></a></li>
        </ul>
        <div className="copyright">Copyright &copy; 2021 AloTech</div>
        <BackTop>
          <div className="goTop"><i className="fas fa-arrow-circle-up"></i></div>
        </BackTop>
      </div>
    </div>
  );
}

export default AppFooter;