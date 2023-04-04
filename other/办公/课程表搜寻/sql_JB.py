import xlrd
if __name__=="__main__":
    data = xlrd.open_workbook(r'管理员.xls')
    table = data.sheets()[0]
    text_='''USE [master]
GO
/****** Object:  Database [管理员]    Script Date: 2023/4/2 22:31:18 ******/
CREATE DATABASE [管理员]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'管理员', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\管理员.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'管理员_log', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\管理员_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [管理员] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [管理员].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [管理员] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [管理员] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [管理员] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [管理员] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [管理员] SET ARITHABORT OFF 
GO
ALTER DATABASE [管理员] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [管理员] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [管理员] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [管理员] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [管理员] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [管理员] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [管理员] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [管理员] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [管理员] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [管理员] SET  DISABLE_BROKER 
GO
ALTER DATABASE [管理员] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [管理员] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [管理员] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [管理员] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [管理员] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [管理员] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [管理员] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [管理员] SET RECOVERY FULL 
GO
ALTER DATABASE [管理员] SET  MULTI_USER 
GO
ALTER DATABASE [管理员] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [管理员] SET DB_CHAINING OFF 
GO
ALTER DATABASE [管理员] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [管理员] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [管理员] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'管理员', N'ON'
GO
ALTER DATABASE [管理员] SET QUERY_STORE = OFF
GO
USE [管理员]
GO
/****** Object:  Table [dbo].[管理员]    Script Date: 2023/4/2 22:31:18 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[管理员](
	[学生姓名] [varchar](10) NULL,
	[性别] [varchar](3) NULL,
	[学号] [int] NULL,
	[账号] [int] NULL,
	[密码] [int] NULL,
	[年级] [varchar](15) NULL,
	[科目] [varchar](15) NULL
) ON [PRIMARY]
GO\nINSERT [dbo].[管理员] ([学生姓名], [性别], [学号], [账号], [密码], [年级], [科目]) VALUES '''
    for i in range(1,table.nrows):
        a=table.row(i)
        text_+=(r"(N'{}', N'{}', {}, {}, {}, N'{}', N'高等数学')".format(a[0].value,a[1].value,int(a[2].value),int(a[3].value),int(a[4].value),a[5].value)+',\n')
    text_+='''USE [master]
GO
ALTER DATABASE [管理员] SET  READ_WRITE 
GO'''
    with open('管理员.sql','w') as f:
        f.write(text_)