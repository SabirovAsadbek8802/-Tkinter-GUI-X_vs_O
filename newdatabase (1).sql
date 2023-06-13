-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 12 2023 г., 07:06
-- Версия сервера: 10.4.27-MariaDB
-- Версия PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `new_data_base_db`
--

-- --------------------------------------------------------

--
-- Структура таблицы `newdatabase`
--

CREATE TABLE `newdatabase` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `newdatabase`
--

INSERT INTO `newdatabase` (`id`, `username`, `login`, `password`, `email`, `phone`) VALUES
(6, 'Asadbek', 'Asadbek8802', '885108802a', 'sabirov@gmail.com', '885108802'),
(7, 'a', 'a', 'a', 'a', 'a'),
(8, 'Jakhongir', 'Jaxa_vorovskoy', '12345', 'Jakhongir2009@gmail.com', '456961');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `newdatabase`
--
ALTER TABLE `newdatabase`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`,`email`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `newdatabase`
--
ALTER TABLE `newdatabase`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
