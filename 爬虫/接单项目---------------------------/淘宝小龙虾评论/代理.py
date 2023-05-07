def is_pass(arr_all:ArrayBuffer[String]): ArrayBuffer[String]  = {
      val arr_pass = ArrayBuffer[String]()
      for ( i <- arr_all) {
      try{
        //proxy(ip,port)这个函数添加ip进header
        val response = Jsoup.connect("https://s.taobao.com/search?q=%E5%B0%8F%E9%BE%99%E8%99%BE&sort=sale-desc").proxy(i.split(":").head.trim,i.split(":").last.trim.toInt).userAgent(agent).execute()

        if(response.statusCode()!=200){
          println("Bad proxy: "+i)
        }
        else {
          arr_pass.append(i)
          println("Success  proxy: "+i)
        }

      }
      catch{
        case e => println(e)
      }

    }
    arr_pass
  }