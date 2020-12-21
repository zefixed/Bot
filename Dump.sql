-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               8.0.21 - MySQL Community Server - GPL
-- Операционная система:         Win64
-- HeidiSQL Версия:              11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Дамп структуры базы данных testdb
CREATE DATABASE IF NOT EXISTS `testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `testdb`;

-- Дамп структуры для таблица testdb.algebraic_concepts
CREATE TABLE IF NOT EXISTS `algebraic_concepts` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `edu_mat` text,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ft1` (`question`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы testdb.algebraic_concepts: 39 rows
/*!40000 ALTER TABLE `algebraic_concepts` DISABLE KEYS */;
INSERT INTO `algebraic_concepts` (`id`, `question`, `answer`, `edu_mat`) VALUES
	(1, 'Площадь квадрата 49 см 2. Чему равен его периметр? Gkjoflm rdflhfnf 49 cv 2/ Xtve hfdty tuj gthbvtnh&', '28см', 'https://clck.ru/SJxQt'),
	(2, 'Каким словом обозначался миллион в Древней Руси? Rfrbv ckjdjv j,jpyfxfkcz vbkkbjy d Lhtdytq Hecb&', 'Тьма', 'https://clck.ru/SJxRX'),
	(3, 'Какие цифры употребляются в десятичной системе? Rfrbt wbahs egjnht,kz.ncz d ltcznbxyjq cbcntvt&', 'Арабские', 'https://clck.ru/SJxTm'),
	(4, 'Что означает слово конус в переводе с греческого? Xnj jpyfxftn ckjdj rjyec d gthtdjlt c uhtxtcrjuj&', 'Сосновая шишка', 'https://clck.ru/SJxU8'),
	(6, 'Для какого четырехугольника имеет смысл выражение: «Найдите среднюю линию» Lkz rfrjuj xtnsht[eujkmybrf bvttn cvsck dshf;tybt^ «Yfqlbnt chtly.. kbyb.»', 'Трапеция', 'https://clck.ru/SJxUp'),
	(7, 'Название какой фигуры в переводе с греческого языка означает «обеденный столик»? Yfpdfybt rfrjq abuehs d gthtdjlt c uhtxtcrjuj zpsrf jpyfxftn «j,tltyysq cnjkbr»&', 'Трапеция', 'https://clck.ru/SJxVB'),
	(8, 'Когда моему отцу было 31 год, мне было 8 лет, а теперь отец старше меня вдвое. Сколько мне лет? Rjulf vjtve jnwe ,skj 31 ujl? vyt ,skj 8 ktn? f ntgthm jntw cnfhit vtyz dldjt/ Crjkmrj vyt ktn&', 'Мне 23 года', 'https://clck.ru/SJxVb'),
	(10, 'На какой угол поворачивается солдат по команде «кругом»? Yf rfrjq eujk gjdjhfxbdftncz cjklfn gj rjvfylt «rheujv»&', 'На 180°', 'https://clck.ru/SJxWN'),
	(11, 'Какая геометрическая фигура нужна для наказания детей? Rfrfz utjvtnhbxtcrfz abuehf ye;yf lkz yfrfpfybz ltntq&', 'Угол', 'https://clck.ru/SJxWv'),
	(12, 'Какие геометрические фигуры дружат с солнцем? Rfrbt utjvtnhbxtcrbt abuehs lhe;fn c cjkywtv&', 'Лучи', 'https://clck.ru/SJxYJ'),
	(13, 'Два сына и два отца съели три яйца. Сколько яиц съел каждый? Ldf csyf b ldf jnwf c]tkb nhb zqwf/ Crjkmrj zbw c]tk rf;lsq&', 'По 1 яйцу', 'https://clck.ru/SJxYe'),
	(15, 'Батон разрезали на три части. Сколько сделали разрезов? <fnjy hfphtpfkb yf nhb xfcnb/ Crjkmrj cltkfkb hfphtpjd&', 'Два', 'https://clck.ru/SJxZR'),
	(18, 'Как называется функция графиком, которой является гипербола? Rfr yfpsdftncz aeyrwbz uhfabrjv? rjnjhjq zdkztncz ubgth,jkf&', 'Обратная пропорциональность', 'https://clck.ru/SJxaJ'),
	(19, 'Как называется сторона треугольника, противолежащая прямому углу? Rfr yfpsdftncz cnjhjyf nhteujkmybrf? ghjnbdjkt;fofz ghzvjve euke&', 'Гипотенуза', 'https://clck.ru/SJxbT'),
	(20, 'Как называется одна трехсотшестидесятая часть круга? Rfr yfpsdftncz jlyf nht[cjnitcnbltcznfz xfcnm rheuf&', 'Градус', 'https://clck.ru/SJxc2'),
	(21, 'Как называются две прямые, которые не пересекаются? Rfr yfpsdf.ncz ldt ghzvst? rjnjhst yt gthtctrf.ncz&', 'Параллельными', 'https://clck.ru/SJxcW'),
	(22, 'Как называется  хорда, проходящая через центр окружности? Rfr yfpsdftncz  [jhlf? ghj[jlzofz xthtp wtynh jrhe;yjcnb&', 'Диаметр', 'https://clck.ru/SJxcv'),
	(23, 'Как называются два угла, у которых одна сторона общая? Rfr yfpsdf.ncz ldf eukf? e rjnjhs[ jlyf cnjhjyf j,ofz&', 'Смежные', 'https://clck.ru/SJxdF'),
	(24, 'Как называется граница шара? Rfr yfpsdftncz uhfybwf ifhf&', 'Сфера', 'https://clck.ru/SJxdb'),
	(26, 'Как называется постоянная величина? Rfr yfpsdftncz gjcnjzyyfz dtkbxbyf& ', 'Константа', 'https://clck.ru/SJxTD'),
	(27, 'Какой знак можно поставить между 2 и 3, чтобы получилось число большее 2 и меньшее 3 Rfrjq pyfr vj;yj gjcnfdbnm vt;le 2 b 3? xnj,s gjkexbkjcm xbckj ,jkmitt 2 b vtymitt 3', 'Запятую', 'https://clck.ru/SJxfu'),
	(28, 'Число, которое после подстановки его в уравнение обращает уравнение в тождество Xbckj? rjnjhjt gjckt gjlcnfyjdrb tuj d ehfdytybt j,hfoftn ehfdytybt d nj;ltcndj', 'Корень', 'https://clck.ru/SJxnU'),
	(29, 'Геометрическая фигура, образованная 2-мя лучами с общим началом Utjvtnhbxtcrfz abuehf? j,hfpjdfyyfz 2-vz kexfvb c j,obv yfxfkjv', 'Угол', 'https://clck.ru/SJxoT'),
	(30, 'Синоним слова «промежуток» Cbyjybv ckjdf «ghjvt;enjr»', 'Интервал', 'https://clck.ru/SJxoj'),
	(31, 'Как называется сотая часть числа? Rfr yfpsdftncz cjnfz xfcnm xbckf&', 'Процент', 'https://clck.ru/SJxpL'),
	(32, 'Как найти неизвестное делимое? Rfr yfqnb ytbpdtcnyjt ltkbvjt&', 'Частное умножить на делитель', 'https://clck.ru/SJxpa'),
	(34, 'Наименьшее натуральное число Yfbvtymitt yfnehfkmyjt xbckj', 'Единица', 'https://clck.ru/SJxqD'),
	(38, 'Веревку разрезали на 12 частей. Сколько раз ее разрезали? Dthtdre hfphtpfkb yf 12 xfcntq/ Crjkmrj hfp tt hfphtpfkb&', '11 раз', 'https://clck.ru/SJxsZ'),
	(40, 'Наука о числах, их свойствах и действиях над ними Yferf j xbckf[? b[ cdjqcndf[ b ltqcndbz[ yfl ybvb', 'Арифметика', 'https://clck.ru/SJxuM'),
	(41, 'Место, занимаемое цифрой и записи числа Vtcnj? pfybvftvjt wbahjq b pfgbcb xbckf', 'Разряд', 'https://clck.ru/SJxwd'),
	(42, 'Сколько корней имеет квадратное уравнение, если дискриминант больше 0 Crjkmrj rjhytq bvttn rdflhfnyjt ehfdytybt? tckb lbcrhbvbyfyn ,jkmit 0', 'Два', 'https://clck.ru/SJxwq'),
	(43, 'Кто ввел прямоугольную систему координат Rnj ddtk ghzvjeujkmye. cbcntve rjjhlbyfn ', 'Рене Декарт', 'https://clck.ru/SJxxA'),
	(44, 'Цифровой знак, обозначающий отсутствие величины Wbahjdjq pyfr? j,jpyfxf.obq jncencndbt dtkbxbys', 'Ноль', 'https://clck.ru/SJxxJ'),
	(45, 'Треугольник со сторонами 3, 4, 5. Nhteujkmybr cj cnjhjyfvb 3б 4б 5ю ', 'Египетский', 'https://clck.ru/SJxyB'),
	(46, 'Кому принадлежит восклицание : «А все – таки она вертится?» Rjve ghbyflkt;bn djcrkbwfybt ^ «F dct – nfrb jyf dthnbncz&»', 'Галилео Галилей', 'https://clck.ru/SJxyP'),
	(47, 'На какое наименьшее целое число делится без остатка целое число? Yf rfrjt yfbvtymitt wtkjt xbckj ltkbncz ,tp jcnfnrf wtkjt xbckj&', '1', 'https://clck.ru/SJxz2'),
	(48, 'Другое название независимой переменной Lheujt yfpdfybt ytpfdbcbvjq gthtvtyyjq', 'Аргумент', 'https://clck.ru/SJxzc'),
	(49, 'Уравнение второй степени Ehfdytybt dnjhjq cntgtyb', 'Квадратное', 'https://clck.ru/SJxzn'),
	(50, 'Утверждение, которое не доказывается Endth;ltybt? rjnjhjt yt ljrfpsdftncz', 'Аксиома', 'https://clck.ru/SJy23');
/*!40000 ALTER TABLE `algebraic_concepts` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.easter_egg
CREATE TABLE IF NOT EXISTS `easter_egg` (
  `id` int NOT NULL DEFAULT '0',
  `cookies` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы testdb.easter_egg: ~0 rows (приблизительно)
/*!40000 ALTER TABLE `easter_egg` DISABLE KEYS */;
INSERT INTO `easter_egg` (`id`, `cookies`) VALUES
	(1, 57);
/*!40000 ALTER TABLE `easter_egg` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.feedback
CREATE TABLE IF NOT EXISTS `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `problem` text,
  `request` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы testdb.feedback: ~8 rows (приблизительно)
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` (`id`, `user_id`, `problem`, `request`) VALUES
	(8, 739239599, NULL, '/info'),
	(9, 739239599, '/start', NULL),
	(10, 479358154, NULL, 'Предложение'),
	(11, 479358154, NULL, 'Предложение'),
	(12, 479358154, 'Проблема', NULL),
	(13, 479358154, NULL, 'Предложение'),
	(14, 479358154, 'Описание проблемы', NULL),
	(15, 479358154, 'Описание проблемы', NULL);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.geometric_concepts
CREATE TABLE IF NOT EXISTS `geometric_concepts` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `edu_mat` text,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ft1` (`question`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы testdb.geometric_concepts: 50 rows
/*!40000 ALTER TABLE `geometric_concepts` DISABLE KEYS */;
INSERT INTO `geometric_concepts` (`id`, `question`, `answer`, `edu_mat`) VALUES
	(1, 'Точка Njxrf', 'Это основная фигура для абсолютно всех построений,обозначать буквой латинской алфавита, к примеру, A, B, K, L.', 'https://clck.ru/JNS9T'),
	(2, 'Прямая Ghzvfz', 'Это фигура полностью размещается в одной плоскости. У прямой нет конкретного математического определения, так как она состоит из огромного количества точек.', 'https://clck.ru/9cKgB'),
	(3, 'Угол Eujk', 'Угол - это конструкция, состоящая из вершины и двух лучей, которые выходят из нее. То есть стороны этой фигуры соединяются в одной точке.', 'https://clck.ru/SHpQb'),
	(4, 'Плоскость Gkjcrjcnm', 'Это фигура, у которой нет ни конца, ни начала, равно как и прямой, и точки', 'https://clck.ru/SHpgR'),
	(5, 'Прямоугольник Ghzvjeujkmybr', 'Это параллелограмм, у которого все стороны соприкасаются под прямым углом.', 'https://clck.ru/SHph2'),
	(6, 'Параллелограмм Gfhfkktkjuhfvv', 'Это геометрическая фигура, противоположные стороны которой параллельны друг другу попарно', 'https://clck.ru/SHphY'),
	(7, 'Квадрат Rdflhfn', 'Это четырехугольник с равными сторонами и углами.', 'https://clck.ru/9cVVJ'),
	(8, 'Ромб Hjv,', 'Это фигура, у которой все грани равны. При этом углы могут быть совершенно разными, но попарно', 'https://clck.ru/SHpWs'),
	(9, 'Трапеция Nhfgtwbz', 'Это фигура, которая чем-то схожа с четырехугольником. Она имеет две параллельные противоположные стороны и при этом считается криволинейной.', 'https://clck.ru/SHpXi'),
	(10, 'Круг Rheu', 'Эта геометрическая фигура подразумевает расположение на одной плоскости точек, равноудаленных от ее центра', 'https://clck.ru/9cJqa'),
	(11, 'Треугольник Nhteujkmybr', 'Это простая геометрическая фигура, которая очень часто встречается и изучается.', 'https://clck.ru/SHpc3'),
	(12, 'Многоугольник Vyjujeujkmybr', 'Вершинами многоугольников называют точки, соединяющие отрезки. А последние, в свою очередь, принято считать сторонами.', 'https://clck.ru/SHpdW'),
	(13, 'Отрезок Jnhtpjr', 'Это часть прямой, которая ограничена двумя точками', 'https://clck.ru/SHpiX'),
	(14, 'Призма Ghbpvf', 'Многогранник, две грани которого являются конгруэнтными многоугольниками, лежащими в параллельных плоскостях, а остальные грани — параллелограммами, имеющими общие стороны с этими многоугольникам', 'https://clck.ru/SHpjx'),
	(15, 'Луч Kex', 'Часть прямой, состоящая из данной точки и всех точек, лежащих по одну сторону от неё.', 'https://clck.ru/J4M5K'),
	(16, 'Острый угол Jcnhsq eujk', 'Угол до 90 градусов', 'https://clck.ru/SHpnK'),
	(17, 'Прямой угол Ghzvjq eujk', 'Угол 90 градусов', 'https://clck.ru/SHpnK'),
	(18, 'Тупой угол Negjq eujk', 'Угол больше 90 градусов', 'https://clck.ru/SHpnK'),
	(19, 'Смежный угол Cvt;ysq eujk', 'Смежными углами называются два прилежащих угла, несовпадающие стороны которых образуют прямую', 'https://clck.ru/SHppD'),
	(20, 'Вертикальный угол Dthnbrfkmysq eujk', 'Это пары углов с общей вершиной, которые образованы при пересечении двух прямых так, что стороны одного угла являются продолжением сторон другого.', 'https://clck.ru/NmLPf'),
	(21, 'Перпендикулярные прямые Gthgtylbrekzhyst ghzvst', 'Две прямые в пространстве перпендикулярны друг другу, если они соответственно параллельны некоторым двум другим взаимно перпендикулярным прямым, лежащим в одной плоскости.', 'https://clck.ru/SHprf'),
	(22, 'Параллельные прямые Gfhfkktkmyst ghzvst', 'Прямые, которые не пересекаются, сколько бы их ни продолжали в обе стороны.', 'https://clck.ru/SHpsc'),
	(23, 'Центральный угол Wtynhfkmysq eujk', 'Центральный угол - это угол, вершина которого является центром O окружности, а ноги - это радиусы, пересекающие окружность в двух разных точках A и B', 'https://clck.ru/SHpwa'),
	(24, 'Вписанный угол Dgbcfyysq eujk', 'Это угол, вершина которого лежит на окружности, а стороны пересекают эту окружность.', 'https://clck.ru/SHpxm'),
	(25, 'Биссектриса <bcctrnhbcf', 'Биссектриса это крыса, ходит по углам и делит угол пополам', 'https://clck.ru/SHpyJ'),
	(26, 'Медиана Vtlbfyf', 'Отрезок, соединяющий вершину треугольника с серединой противоположной стороны.', 'https://clck.ru/SHq26'),
	(27, 'Высота Dscjnf', 'Отрезок перпендикуляра, опущенного из вершины геометрической фигуры', 'https://clck.ru/SHq4i'),
	(28, 'Вектор Dtrnjh', 'Простейшем случае математический объект, характеризующийся величиной и направлением.', 'https://clck.ru/ErgDW'),
	(29, 'Синус Cbyec', 'Это отношение длины стороны, противоположной этому углу, к длине самой длинной стороны треугольника.', 'https://clck.ru/SHq77'),
	(30, 'Косинус Rjcbyec', 'Это отношение прилежащего катета к гипотенузе.', 'https://clck.ru/SHq77'),
	(31, 'Тангенс Nfyutyc', 'Отношение синуса к косинусу (т. е. tg = sin/cos) или отношение противолежащего катета к прилежащему', 'https://clck.ru/SHq77'),
	(32, 'Котангенс Rjnfyutyc', 'Это отношение прилежащего (близкого) катета к противолежащему (дальнему).', 'https://clck.ru/SHq77'),
	(33, 'Правильный многоугольник Ghfdbkmysq vyjujeujkmybr', 'Выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.', 'https://clck.ru/SHq9j'),
	(34, 'Куб Re,', 'Правильный шестигранник, все грани к-рого — квадраты.', 'https://clck.ru/9cVhK'),
	(35, 'Шар Ifh', 'Геометрическое тело, образованное вращением круга вокруг своего диаметра.', 'https://clck.ru/NBa5q'),
	(36, 'Цилиндр Wbkbylh', 'Геометрическое тело, ограниченное цилиндрической поверхностью и двумя параллельными плоскостями, пересекающими её', 'https://clck.ru/SHqCi'),
	(37, 'Параллелепипед Gfhfkktktgbgtl', 'Многогранник с шестью гранями, каждая из которых является в общем случае прямоугольником.', 'https://clck.ru/SHphY'),
	(38, 'Пирамида Gbhfvblf', 'Многогранник, одна из граней которого — произвольный многоугольник, а остальные грани — треугольники, имеющие общую вершину.', 'https://clck.ru/JeSaC'),
	(39, 'Конус Rjyec', 'Геометрическое тело, образуемое вращением прямоугольного треугольника вокруг катета', 'https://clck.ru/SHqFm'),
	(40, 'Октаэдр Jrnf\'lh', 'Многогранник с восемью гранями.', 'https://clck.ru/SHqGe'),
	(41, 'Тетраэдр Ntnhf\'lh', 'Простейший многогранник, гранями которого являются четыре треугольника', 'https://clck.ru/SHqJ8'),
	(42, 'Многогранники Vyjujuhfyybrb', 'Обычно замкнутая поверхность, составленная из многоугольников', 'https://clck.ru/R4sXx'),
	(43, 'Призмаотид Ghbpvfjnbl', 'Многогранник, ограниченный двумя многоугольниками, расположенными в параллельных плоскостях (они являются его основаниями); его боковые грани представляют собой треугольники или трапеции, вершины которых являются и вершинами многоугольников оснований', 'https://clck.ru/SHqLW'),
	(44, 'Гексаэдр Utrcf\'lh', 'Это куб состоящий из шести равных квадратов.', 'https://clck.ru/SHqMZ'),
	(45, 'Додекаэдр Ljltrf\'lh', 'Правильный двенадцатигранник, состоит из двенадцати правильных и равных пятиугольников, соединенных по три около каждой вершины', 'https://clck.ru/Rbu5w'),
	(46, 'Икосаэдр Brjcf\'lh', 'Состоит из 20 равносторонних и равных треугольников, соединенных по пять около каждой вершины', 'https://clck.ru/9vxF3'),
	(47, 'Ломаная линия Kjvfyfz kbybz', 'Это фигура, которая состоит из отрезков, последовательно соединенных своими концами.', 'https://clck.ru/SHqR9'),
	(48, 'Кривая линия Rhbdfz kbybz', 'Это плавно изгибающаяся линия, которая определяется расположением составляющих её точек.', 'https://clck.ru/SHqSS'),
	(49, 'Незамкнутая линия Ytpfvryenfz kbybz', 'Это линия, концы которой не соединены вместе.', 'https://clck.ru/SHqSS'),
	(50, 'Замкнутая линия Pfvryenfz kbybz', 'Это линия, концы которой соединены вместе.', 'https://clck.ru/SHqSS');
/*!40000 ALTER TABLE `geometric_concepts` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.probability_theory
CREATE TABLE IF NOT EXISTS `probability_theory` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `edu_mat` text,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ft1` (`question`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы testdb.probability_theory: 50 rows
/*!40000 ALTER TABLE `probability_theory` DISABLE KEYS */;
INSERT INTO `probability_theory` (`id`, `question`, `answer`, `edu_mat`) VALUES
	(1, 'Событие Cj,snbt', 'Результат опыта или наблюдения ', 'https://clck.ru/SARGz'),
	(2, 'Случайные события Ckexfqyst cj,snbz', 'Опыт, в результате которого может произойти или не произойти событие ', 'https://clck.ru/SJDft'),
	(3, 'Теория вероятностей Ntjhbz dthjznyjcntq', 'Раздел математики, изучающий случайные события', 'https://clck.ru/SJDsi'),
	(4, 'Единственно возможные события Tlbycndtyyj djpvj;yst cj,snbz', 'Когда в опыте происходит только одно событие ', 'https://clck.ru/SJECQ'),
	(5, 'Равновозможное событие Hfdyjdjpvj;yjt cj,snbt', 'Когда события могут произойти с одинаковой вероятностью ', 'https://clck.ru/SJECQ'),
	(6, 'Достоверное событие Ljcnjdthyjt cj,snbt ', 'Событие, которое обязательно произойдёт ', 'https://clck.ru/SJECQ'),
	(7, 'Несовместные события Ytcjdvtcnyst cj,snbz', 'События, которые не могут произойти в одно время', 'https://clck.ru/SJECQ'),
	(8, 'Сумма событий Cevvf cj,snbq ', 'Событие, в котором происходит одно из событий А и В', 'https://clck.ru/SJECQ'),
	(9, 'Произведение событий Ghjbpdtltybt cj,snbq', 'Событие, в котором происходят оба события и А, и В', 'https://clck.ru/SJECQ'),
	(10, 'Противоположные события Ghjnbdjgjkj;yst cj,snbz', 'Два единственно возможные события', 'https://clck.ru/SJECQ'),
	(11, 'Как называют число m/n Rfr yfpsdf.n xbckj m/n', 'Называют относительной частотой события А ', 'https://clck.ru/SJECQ'),
	(12, 'Статистическая устойчивость относительных частот Cnfnbcnbxtcrfz ecnjqxbdjcnm jnyjcbntkmys[ xfcnjn', 'Это когда относительная частота события мало отличается от вероятности события ', 'https://clck.ru/SJEpe'),
	(13, 'Статистичекое определение вероятности Cnfnbcnbxtrjt jghtltktybt dthjznyjcnb ', 'Это когда относительную частоту принимаем за приближённое значение вероятности ', 'https://clck.ru/SJEx6'),
	(14, 'Аксиоматическое определение вероятности Frcbjvfnbxtcrjt jghtltktybt dthjznyjcnb ', 'В нём определение вероятности задаётся перечеслением её свойств ', 'https://clck.ru/SJF7e'),
	(15, 'Элементарная теория вероятностей "ktvtynfhyfz ntjhbz dthjznyjcntq ', 'Теория, изучающая вероятность событий лишь для опытов с конечным числом исходов ', 'https://clck.ru/SJFEd'),
	(16, 'Общая теория вероятностей J,ofz ntjhbz dthjznyjcntq', 'Теория, с бесконечным числом возможных событий ', 'https://clck.ru/SJFMt'),
	(17, 'Условная вероятность событий В, при условии, что произошло событие А Eckjdyfz dthjznyjcnm cj,snbq В, ghb eckjdbb, xnj ghjbpjikj cj,snbt А', 'Называют отношение числа случаев благоприпятствующих событию АВ', 'https://clck.ru/SJRPJ'),
	(18, 'Когда события А и В называют независимыми? Rjulf cj,snbz А b В yfpsdf.n ytpfdbcbvsvb?', 'Когда справедливо равенство ', 'https://clck.ru/SJRPJ'),
	(19, 'Случайная величина х Ckexfqyfz dtkbxbyf х', 'Когда каждому событию В она ставит определённое число х', 'https://clck.ru/SJRSo'),
	(20, 'Математическое ожидание Vfntvfnbxtcrjt j;blfybt', 'Это число обозначаемое М, равное сумме произведений значений случайной величины', 'https://clck.ru/SJRTn'),
	(21, 'Математическое ожидание случаной величины Vfntvfnbxtcrjt j;blfybt ckexfyjq dtkbxbys ', 'Среднее взвешенное(вероятностями) её значений', 'https://clck.ru/SJRUj'),
	(22, 'Что принимает случайная величина Х? Xnj ghbybvftn ckexfqyfz dtkbxbyf Х?', 'Она принимает значения , равные числу выпавших очков', 'https://clck.ru/SJRUj'),
	(23, 'Случайная велечина Х Ckexfqyfz dtktxbyf Х', 'Количество очков выбиваемых первым стрелком', 'https://clck.ru/SJRTn'),
	(24, 'Случайная велечина y Ckexfqyfz dtktxbyf y', 'Количество очков выбиваемых вторым стрелком', 'https://clck.ru/SJRTn'),
	(25, 'С чем возникло понятие математического ожидания C xtv djpybrkj gjyznbt vfntvfnbxtcrjuj j;blfybz', 'Возникло в связи с изучением азартных игр', 'https://clck.ru/SJRTn'),
	(26, 'Независимый опыт Ytpfdbcbvsq jgsn', 'Это опыт, в котором вероятность появления какого либо события А в каждом опыте не зависит от его присутствия в других опытах', 'https://clck.ru/SJRUj'),
	(27, 'В чём заключается вероятность события D x`v pfrk.xftncz dthjznyjcnm cj,snbz', 'В том, что в первом опыте происходит событие А, во втором, В', 'https://clck.ru/SJRZc'),
	(28, 'Как называют события А1, А2,... Rfr yfpsdf.n cj,snbz А1, А2,...', 'Их называют единственно возможными', 'https://clck.ru/SJRbi'),
	(29, 'Как называют события С1, С2,... Rfr yfpsdf.n cj,snbz С1, С2,...', 'Их называют равновозможными', 'https://clck.ru/SJRdN'),
	(30, 'Как называют события А и В Rfr yfpsdf.n cj,snbz А и В', 'Их называют несовместными', 'https://clck.ru/SJRdN'),
	(31, 'В каком случае событие является невозможным D rfrjv ckexft cj,snbt zdkztncz ytdjpvj;ysv', 'Если нет случаев, благоприпятствующих этому событию ', 'https://clck.ru/SJRdN'),
	(32, 'В каком случае событие является достоверным D rfrjv ckexft cj,snbt zdkztncz ljcnjdthysv', 'Если событию благоприпятствуют все рассматриваемые случаи', 'https://clck.ru/SJRfJ'),
	(33, 'В каком случае событие является несовместными D rfrjv ckexft cj,snbt zdkztncz ytcjdvtcnysvb', 'Если при бросании игральной кости событие А есть выпадание или 1, или 2 очков, а событие В выпадание 3 очков', 'https://clck.ru/SJRhS'),
	(34, 'Когда P равно 0 Rjulf P hfdyj 0', 'Если события А и В несовместны', 'https://clck.ru/SJRjU'),
	(35, 'Чему равна x, если значения случайной величины х имеют одну и ту же вероятность p Xtve hfdyf x, tckb pyfxtybz ckexfqyjq dtkbxbys х bvt.n jlye b ne ;t dthjznyjcnm p', 'X равно среднему арифметическому её значений', 'https://clck.ru/SJRok'),
	(36, 'Чему поспособствало открытие азартных игр Xtve gjcgjcj,cndfkj jnrhsnbt fpfhnys[ buh', 'Они поспособствовали зарождению и становлению камбинаторики и теории вероятностей ', 'https://clck.ru/SJRsz'),
	(37, 'Где встречались задачи о дележе ставки? Ult dcnhtxfkbcm pflfxb j ltkt;t cnfdrb?', 'В рукописных арифметических учебниках XIII века', 'https://clck.ru/SJRui'),
	(38, 'До какого века задачи о дележе оставались нерешёнными Lj rfrjuj dtrf pflfxb j ltkt;t jcnfdfkbcm ythti`yysvb', 'Задачи о дележе ставки оставались нерешёнными до середины XVII века', 'https://clck.ru/SJRwk'),
	(39, 'Кто решил задачи о дележе ставки Rnj htibk pflfxb j ltkt;t cnfdrb', 'Паскаль', 'https://clck.ru/SJS3T'),
	(40, 'В чём заключается вероятность события А1, А2..., Аn D x`v pfrk.xftncz dthjznyjcnm cj,snbz А1, А2..., Аn', 'В первом опыте произойдёт событие А1, во втором А2', 'https://clck.ru/SJS3T'),
	(41, 'Какова вероятность того, что при бросании игральной кости 4 раза, хотя бы один раз выпадет 6 очков Rfrjdf dthjznyjcnm njuj? xnj ghb ,hjcfybb buhfkmyjq rjcnb 4 hfpf? [jnz ,s jlby hfp dsgfltn 6 jxrjd', '0,518', 'https://clck.ru/SJS79'),
	(42, 'Какова вероятность того, что одно очко выпадет только в первый, четвёртый и пятый раз Rfrjdf dthjznyjcnm njuj? xnj jlyj jxrj dsgfltn njkmrj d gthdsq? xtnd`hnsq b gznsq hfp', '5^2/6^5', 'https://clck.ru/SJSAJ'),
	(43, 'Что такое комбинаторика Xnj nfrjt rjv,byfnjhbrf', 'Раздел математики в котором разрабатываются различные способы получения комбинаций и методы подсчёта их количества ', 'https://clck.ru/SJSDF'),
	(44, 'Дисперсия Lbcgthcbz', 'Математическое ожидание квадрата отклонения случайной величины от её математического ожидания ', 'https://clck.ru/SJSFd'),
	(45, 'Асимметрия Fcbvvtnhbz', 'Отношение центрального момента третьего порядка к кубу среднеквадратического отклонения', 'https://clck.ru/SJSLt'),
	(46, 'Функция распределения Aeyrwbz hfcghtltktybz ', 'Функция, определяющая вероятность того, что Х примет значение меньше х', 'https://clck.ru/SJSJ6'),
	(47, 'Условная вероятность Eckjdyfz dthjznyjcnm ', 'Вероятность наступления интересующего нас события, связанная с дополнительными условиями ', 'https://clck.ru/SJSQU'),
	(48, 'Регрессия Htuhtccbz', 'Представление одной случайной величины как функции другой', 'https://clck.ru/SJSRj'),
	(49, 'Производящая функция  Ghjbpdjlzofz aeyrwbz ', 'Функция, определяющая вероятность наступления события при различных вероятностях появления в каждом испытании', 'https://clck.ru/SJSSS'),
	(50, 'Общая дисперсия J,ofz lbcgthcbz', 'Дисперсия значений признака всей совокупности относительно общей средней', 'https://clck.ru/SJSTm');
/*!40000 ALTER TABLE `probability_theory` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.radical_power_logarithm
CREATE TABLE IF NOT EXISTS `radical_power_logarithm` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `edu_mat` text,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ft1` (`question`)
) ENGINE=MyISAM AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы testdb.radical_power_logarithm: 49 rows
/*!40000 ALTER TABLE `radical_power_logarithm` DISABLE KEYS */;
INSERT INTO `radical_power_logarithm` (`id`, `question`, `answer`, `edu_mat`) VALUES
	(2, 'Натуральный ряд Yfnehfkmysq hzl', 'Последовательность всех натуральных чисел, \n в порядке возрастания, называется натуральным рядом', 'https://clck.ru/S4YMk'),
	(3, 'Числовые промежутки Xbckjdst ghjvt;enrb', 'Это числовые множества , которые можно изобразить на координатной прямой. \n числовым промежуткам относятся лучи, отрезки, интервалы и полуинтервалы', 'https://clck.ru/S4YUd'),
	(4, 'Луч или полупрямая Kex bkb gjkeghzvfz', 'Часть прямой, состоящая из данной точки и всех точек, лежащих по одну сторону от неё', 'https://clck.ru/S4YUd'),
	(5, 'Открытый луч Jnrhsnsq kex', 'Это множество точек прямой, лежащих по одну сторону от граничной точки, \n не входит в данное множество.', 'https://clck.ru/S4YUd'),
	(6, 'Закрытый луч Pfrhsnsq kex', 'Это множество точек прямой, лежащих по одну сторону от граничной точки, \n данному множеству', 'https://clck.ru/S4YUd'),
	(7, 'Отрезок Jnhtpjr', 'Это множество точек прямой, лежащих между двумя граничными точками, данному множеству.', 'https://clck.ru/S4YUd'),
	(8, 'Интервал Bynthdfk', 'Это множество точек прямой, лежащих между двумя граничными точками, \n принадлежащими данному множеству. Такие множества задаются двойными строгими неравенствами.', 'https://clck.ru/S4Ye3'),
	(9, 'Полуинтервал Gjkebynthdfk', 'Это множество точек прямой, лежащих между двумя граничными точками, \n из которых принадлежит множеству, а другая не принадлежит', 'https://clck.ru/S4Ymt'),
	(10, 'Целые числа Wtkst xbckf', 'Целые числа — расширение множества натуральных чисел, \n добавлением к нему нуля и отрицательных чисел', 'https://clck.ru/N9xuR'),
	(11, 'Рациональное число Hfwbjyfkmyjt xbckj', 'Число, которое можно представить обыкновенной дробью, \n — целое число, а знаменатель — натуральное число.', 'https://clck.ru/L8773'),
	(12, 'Объединение  множеств J,]tlbytybt  vyj;tcnd', 'Это множество, в котором каждый элемент является элементом одного из исходных множеств', 'https://clck.ru/S4ZLY'),
	(13, 'Пересечение множеств Gthtctxtybt vyj;tcnd', 'Это множество, которое состоит из \n общих элементов исходных множеств.', 'https://clck.ru/S4ZNW'),
	(14, 'Принцип математической индукции Ghbywbg vfntvfnbxtcrjq bylerwbb', 'Если свойство, зависящее от натурального числа n , во-первых , верно при n=1 и ,\n во-вторых , из предположения , что оно верно для n=k, следует , что оно верно при n=k+1 , \nто считают , что это свойство верно для любого натурального числа n', 'https://clck.ru/9KX38'),
	(15, 'Доказательство по индукции Ljrfpfntkmcndj gj bylerwbb', 'Это доказательство, основанное на принципе математической индукции', 'https://clck.ru/S27a4'),
	(16, 'N факториал Т afrnjhbfk', 'Функция, определённая на множестве неотрицательных целых чисел', 'https://clck.ru/CNhsB'),
	(17, 'Перестановка из n элементов Gthtcnfyjdrf bp т \'ktvtynjd', 'Это расположение их в определенном порядке', 'https://clck.ru/S4Zcp'),
	(18, 'Сочетание из данных n элементов по k Cjxtnfybt bp lfyys[ т \'ktvtynjd gj л', 'Сочетанием из n элементов по k называется всякая совокупность попарно различных k элементов, \n каким-либо способом из данных n элементов', 'https://clck.ru/S4ZjK'),
	(19, 'Числовое неравенство Xbckjdjt ythfdtycndj', 'Это неравенство, в записи которого по обе стороны от знака неравенства находятся числа или числовые выражения.', 'https://clck.ru/S4ZoR'),
	(20, 'Простое число Ghjcnjt xbckj', 'Если у натурального числа n>1 нет других делителей , кроме 1 и n , то это число называют простым', 'https://clck.ru/9PvHx'),
	(21, 'Составное число Cjcnfdyjt xbckj', 'Если у натуртоального числа n>1 есть  делители , отличные от 1 и n ,то это число называют составным', 'https://clck.ru/S4Zvx'),
	(22, 'Основная теорема арифметики Jcyjdyfz ntjhtvf fhbavtnbrb', 'Каждое натуральное число n>1 можно представить единственным образом в виде произведения простых чисел.', 'https://clck.ru/S4Zxt'),
	(23, 'Сравнение по модулю m Chfdytybt gj vjlek. ь', 'Пусть m- данное натуральное число (m>=2) .Целые числа a и b называют сравнимым по модулю m \n каждое из них при делении на m  , если каждое из них при делении на m даёт один и тот же остаток r', 'https://clck.ru/S4a9g'),
	(24, 'Диофантово уравнение Lbjafynjdj ehfdytybt', 'Это уравнение (как правило, с несколькими неизвестными), решение которого ищется в целых (иногда в натуральных) числах.', 'https://clck.ru/S4aC5'),
	(25, 'Рациональное уравнение Hfwbjyfkmyjt ehfdytybt', 'Это такой вид уравнения в которой левая и правая части рациональные выражения.', 'https://clck.ru/S4aDt'),
	(26, 'Одночлен Jlyjxkty', 'Одночленом называют число , букву , произведение букв и чисел', 'https://clck.ru/S4aYo'),
	(27, 'Многочлен Vyjujxkty', 'Многочленом называют сумму нескольких одночленов', 'https://clck.ru/ErhLw'),
	(28, 'Симметрический многочлен Cbvvtnhbxtcrbq vyjujxkty', 'Многочлен от переменных, не изменяющийся при всех перестановках входящих в него переменных.', 'https://clck.ru/S4acZ'),
	(29, 'Наибольший общий  многочленов A и B Yfb,jkmibq j,obq  vyjujxktyjd Ф b И', 'Наибольшим общим делителем многочленов A и B называют многочлен наибольший степени K<=m, \nна которой делятся на цело и многочлен  A, и многочлен B.', 'https://clck.ru/S4aey'),
	(30, 'Теормема Безу Ntjhvtvf <tpe', 'Остаток от деления многочлена P(x) на двучлен (x-n) равен P(a)', 'https://clck.ru/S4ahg'),
	(31, 'Корень многочлена Rjhtym vyjujxktyf', 'Корнем многочлена называют значение переменной , при которой он обращается в ноль', 'https://clck.ru/S4aiu'),
	(32, 'Схема Горнера C[tvf Ujhythf', 'Алгоритм вычисления значения многочлена, записанного в виде суммы мономов, при заданном значении переменной', 'https://clck.ru/MTdtG'),
	(33, 'Рациональное уравнение неизвестной x Hfwbjyfkmyjt ehfdytybt ytbpdtcnyjq ч', 'Уравнение,левая и правая части которого есть рациональные выражения относительно x, \n рациональным уравнением с неизвестным x', 'https://clck.ru/S284o'),
	(34, 'Корень уравнения Rjhtym ehfdytybz', 'Корнем (или решением) уравнения с неизвестным x называют число, \n подстановке которого уравнения вместо x получается верное числовое равенство', 'https://clck.ru/S4bG2'),
	(35, 'Распадающееся уравнение Hfcgflf.ottcz ehfdytybt', 'Рациональное уравнение называется распадающимся, если его можно представить в виде \n = 0, где P(x) и Q(x) - целые рациональные функции.', 'https://clck.ru/S4bHq'),
	(36, 'Рациональное уравнение с двумя неизвестными x и y Hfwbjyfkmyjt ehfdytybt c ldevz ytbpdtcnysvb ч b н', 'Уравнение , левая и правая части которого есть рациональные выражения относительно x и y, \n рациональным уравнением с двумя неизвестными x и y', 'https://clck.ru/S4bK7'),
	(37, 'Рациональное неравенство с неизвестным x Hfwbjyfkmyjt ythfdtycndj c ytbpdtcnysv ч', 'Неравенство, левая и правая части которого есть рациональные выражения относительно x, \n рациональным неравенством с неизвестным x', 'https://bit.ly/37FYaNJ'),
	(38, 'Метод интервалов Vtnjl bynthdfkjd', 'Это специальный алгоритм, предназначенный для решения сложных неравенств вида f (x) > 0 и f (x) < 0', 'https://clck.ru/Ey5xH'),
	(39, 'Биномиальный коэффицент <byjvbfkmysq rj\'aabwtyn', 'Это коэффициент в разложении бинома Ньютона по степени x.', 'https://clck.ru/M2E7M'),
	(40, 'Алгоритм Евклида Fkujhbnv Tdrkblf', 'Эффективный алгоритм для нахождения наибольшего общего делителя двух целых чисел.', 'https://clck.ru/S4bWc'),
	(41, 'Нестрогие неравенства Ytcnhjubt ythfdtycndf', 'Это неравенства со знаками больше либо равно(>=) или меньше либо равно(<=)', 'https://clck.ru/S28GM'),
	(42, 'Строгие неравенства Cnhjubt ythfdtycndf', 'Это неравенства со знаками сравнения > (больше) или < (меньше)', 'https://clck.ru/S28GM'),
	(43, 'Рациональное нераравенство Hfwbjyfkmyjt ythfhfdtycndj', 'Это неравенство, обе части которого являются рациональными выражениями.', 'https://clck.ru/S28MU'),
	(44, 'Логарифм Kjufhbav', 'Логарифм по основанию a от аргумента x — это степень, в которую надо возвести число a, чтобы получить число x.', 'https://clck.ru/MjccK'),
	(45, 'Корень степени n Rjhtym cntgtyb т', 'Корнем n-й степени из числа a называется такое число t, n-я степень которого равна a', 'https://clck.ru/S4bdj'),
	(46, 'Аргумент Fhuevtyn', 'Независимая переменная', 'https://clck.ru/S4bfo'),
	(47, 'Функция Aeyrwbz', 'Зависимая переменная', 'https://clck.ru/S4bgi'),
	(48, 'Область определения функции J,kfcnm jghtltktybz aeyrwbb', 'Множество X называют областью определения функции y= f(x)', 'https://clck.ru/S4biJ'),
	(49, 'Область изменения функции J,kfcnm bpvtytybz aeyrwbb', 'Множество всех значений зависимой переменной Y называют областью изменения функции y=f(x)', 'https://clck.ru/S28Vt'),
	(50, 'Непрерывная функция Ytghthsdyfz aeyrwbz', 'Если график функции Y=f(x) на некотором промежутке есть непрерывная линия , то функцию называют \n на этом промежутке', 'https://clck.ru/DTqt4');
/*!40000 ALTER TABLE `radical_power_logarithm` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.trigonometry
CREATE TABLE IF NOT EXISTS `trigonometry` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `edu_mat` varchar(50) DEFAULT 'Ссылка удалена',
  PRIMARY KEY (`id`),
  FULLTEXT KEY `ft1` (`question`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы testdb.trigonometry: 50 rows
/*!40000 ALTER TABLE `trigonometry` DISABLE KEYS */;
INSERT INTO `trigonometry` (`id`, `question`, `answer`, `edu_mat`) VALUES
	(1, 'Функция Aeyrwbz', 'Любая функция – это закон, по которому каждому значению независимой переменной соответствует единственное значение зависимой переменной – функции.', 'https://clck.ru/SHpgM'),
	(2, 'Тригонометрическое уравнение Nhbujyjvtnhbxtcrjt ehfdytybt', 'Простейшим тригонометрическим уравнением называется уравнение вида sinx=a, где cos x=a, tgx=a, где a - некоторое действительное число. Решаются они проще всего с помощью тригонометрического круга.', 'https://clck.ru/Shpto'),
	(3, 'Радианная мера Hflbfyyfz vthf', 'Это отношение этого угла к радиану', 'https://clck.ru/SHq2n'),
	(4, 'Тригонометерическая функция числового аргумента Nhbujyjvtnthbxtcrfz aeyrwbz xbckjdjuj fhuevtynf', 'Любая функция – это закон, по которому каждому значению независимой переменной соответствует единственное значение зависимой переменной – функции.', 'https://clck.ru/AQ9CU'),
	(5, 'Косеканс Rjctrfyc', 'Одна из тригонометрических функций, обозначаемая cosec=1/sin', 'https://clck.ru/SHqFX'),
	(6, 'Синус Cbyec', 'Отношение противолежащего катета к гипотенузе', 'https://clck.ru/SHqKy'),
	(7, 'Косинус Rjcbyec', 'Отношение прилежащего катета к гипотенузе', 'https://clck.ru/SHqRh'),
	(8, 'Тангенс Nfyutyc', 'Отношение противолежащего катета к прилежащему', 'https://clck.ru/SHqa6'),
	(9, 'Котангенс Rjnfyutyc', 'Отношение прилежащего катета к противолежащему', 'https://clck.ru/SHqfP'),
	(10, 'Секанс Ctrfyc', 'Отношение гипотенузы к прилежащему катету', 'https://clck.ru/SHqmF'),
	(11, 'Период Gthbjl ', 'Отрезок времени (или другой величины), определённый меткой начала отсчёта периода и меткой конца отсчёта периода. Период функции — величина, добавление которой к аргументу не изменяет значение функции.', 'https://clck.ru/SHsSc'),
	(12, 'Квадратное уравнение Rdflhfnyjt ehfdytybt', 'Алгебраическое уравнение полного вида. где. — неизвестное , — коэффициенты, причём. Выражение. называют квадратным трёхчленом. Корень — это значение переменной. , обращающее квадратный трёхчлен в ноль.', 'https://clck.ru/9YYrC'),
	(13, 'Рациональное уравнение Hfwbjyfkmyjt ehfdytybt', 'Это такой вид уравнения в которой левая и правая части рациональные выражения. В записи уравнения имеются только сложение, вычитание, умножение, деление, а также возведение в целую степень. Любое рациональное уравнение сводится к алгебраическому.', 'https://clck.ru/Shsan'),
	(14, 'Тождество Nj;ltcndj', 'Равенство, выполняющееся на всём множестве значений входящих в него переменных.', 'https://clck.ru/SHseY'),
	(15, 'Тригонометрическое тождество Nhbujyjvtnhbxtcrjt nj;ltcndj', 'Математические выражения для тригонометрических функций, которые выполняются при всех значениях аргумента (из общей области определения). Формула (1.1) является следствием теоремы Пифагора.', 'https://clck.ru/Shshu'),
	(16, 'Однородные уравнения Jlyjhjlyst ehfdytybz', 'Однородным уравнением n-й степени, называется уравнение вида: Такое уравнение после исключения отдельно рассматриваемого случая. и деления уравнения на. сводится с помощью замены. к алгебраическому уравнению.', 'https://clck.ru/SHsmw'),
	(17, 'Корень уравнения Rjhtym ehfdytybz', 'Это число, при подстановке которого в уравнение получается верное равенство', 'https://clck.ru/SHsrJ'),
	(18, 'Простейшее неравенство Ghjcntqitt ythfdtycndj', 'Решением неравенства с двумя переменными называется множество пар чисел которые удовлетворяют этому неравенству (т.е. при подстановке этих точек неравенство верно).', 'https://clck.ru/SHsvt'),
	(19, 'Интервал Bynthdfk', 'Множество всех чисел, удовлетворяющих строгому неравенству.', 'https://clck.ru/S4Ye3'),
	(20, 'Действительное число Ltqcndbntkmyjt xbckj', 'Математический объект, возникший из потребности измерения геометрических и физических величин окружающего мира, а также проведения таких вычислительных операций, как извлечение корня, вычисление логарифмов.', 'https://clck.ru/SHt6u'),
	(21, 'Графическая иллюстрация Uhfabxtcrfz bkk.cnhfwbz', 'Рисунок, фотография, гравюра или другое изображение, поясняющее текст. Художника, выполняющего иллюстрации к тексту, называют иллюстра́тором.', 'https://clck.ru/Gf3Sx'),
	(22, 'График функции Uhfabr aeyrwbb', 'Геометрическое понятие в математике, дающее представление о геометрическом образе функции. Наиболее наглядны графики вещественнозначных функций вещественного переменного одной переменной.', 'https://clck.ru/SHtJX'),
	(23, 'Квадрат неравенства Rdflhfn ythfdtycndf', 'Это такое неравенство, которое имеет вид a*x^2+b*x+c<0, где a, b и c – некоторые числа, причем a не равно нулю. x – это переменная, а на месте знака < может стоять любой другой знак неравенства', 'https://clck.ru/SHtPk'),
	(24, 'Рациональное неравенство Hfwbjyfkmyjt ythfdtycndj', 'Это неравенство с переменными, обе части которого есть рациональные выражения.', 'https://clck.ru/SHtVN'),
	(25, 'Преобразование уравнений Ghtj,hfpjdfybt ehfdytybq', 'Два или более уравнений называются равносильными, если они имеют одни и те же корни. Преобразование - замена одного уравнения другим, равносильным первому.', 'https://clck.ru/SHtfv'),
	(26, 'Уравнение вида Ehfdytybt dblf', 'Равенство вида. , где чаще всего в качестве. выступают числовые функции, хотя на практике встречаются и более сложные случаи — например, уравнения для вектор-функций, функциональные уравнения и другие.', 'https://clck.ru/Shpto'),
	(27, 'Неравенство Ythfdtycndj', 'Отношение, связывающее два числа или иных математических объекта с помощью одного из перечисленных ниже знаков. ', 'https://clck.ru/SHtv9'),
	(28, 'Строгое неравенство Cnhjujt ythfdtycndj', 'Это неравенства со знаками сравнения > (больше) или < (меньше). Нестрогие – это неравенства со знаками сравнения ≥ (больше или равно) или ≤ (меньше или равно)', 'https://clck.ru/SHtzP'),
	(29, 'Промежуток Ghjvt;enjr', 'Множество вещественных чисел, обладающее тем свойством, что вместе с любыми двумя числами содержит любое, лежащее между ними.', 'https://clck.ru/SHu4L'),
	(30, 'Тригонометрия Nhbujyjvtnhbz', 'Раздел математики, в котором изучаются тригонометрические функции и их использование в геометрии. Данный термин впервые появился в 1595 г. как название книги немецкого математика Бартоломеуса Питискуса ', 'https://clck.ru/AUAeQ'),
	(31, 'Окружность Jrhe;yjcnm', 'Замкнутая плоская кривая, все точки которой одинаково удалены от данной точки (центра), лежащей в той же плоскости, что и кривая.', 'https://clck.ru/RfEmE'),
	(32, 'Хорда {jhlf', 'Отрезок, соединяющий две точки данной кривой (например, окружности, эллипса, параболы, гиперболы). Хорда находится на секущей прямой — прямой линии, пересекающей кривую в двух или более точках.', 'https://clck.ru/RfEmE'),
	(33, 'Тригонометрический круг Nhbujyjvtnhbxtcrbq rheu', 'Это просто единичная окружность с центром в начале координат', 'https://clck.ru/SHuCU'),
	(34, 'Тригонометрические неравенства Nhbujyjvtnhbxtcrbt ythfdtycndf', 'Тригонометрическими неравенствами называются неравенства, которые содержат переменную под знаком тригонометрической функции', 'https://clck.ru/SHuG8'),
	(35, 'Тригонометрическая подстановка Nhbujyjvtnhbxtcrfz gjlcnfyjdrf', 'Универсальная тригонометрическая подстановка, в англоязычной литературе называемая в честь Карла Вейерштрасса подстановкой Вейерштрасса, применяется в интегрировании для нахождения первообразных.', 'https://clck.ru/SHuKX'),
	(36, 'Положительный угол Gjkj;bntkmysq eujk', 'Когда объект вращается против часовой стрелке', 'https://clck.ru/SHuPs'),
	(37, 'Отрицательный угол Jnhbwfntkmysq eujk', 'Когда объект вращается по часовой стрелке', 'https://clck.ru/SHuT3'),
	(38, 'Синус угла a Cbyec eukf ф', 'Число, равное ординате точки единичной окружности, соответствующей углу , называют синус a', 'https://clck.ru/SHuaC'),
	(39, 'Косинус угла a Rjcbyec eukf ф', 'Число, равное a, абциссе точки единичной окружности, соответствующей углу , называют косинусом угла a', 'https://clck.ru/Shudm'),
	(40, 'Арксинус Fhrcbyec', 'Это обратная тригонометрическая функция', 'https://clck.ru/Shugp'),
	(41, 'Арксинус числа a Fhrcbyec xbckf ф', 'Это угол −90°≤α≤90° (−π/2≤α≤π/2), синус которого равен a.', 'https://clck.ru/SHunU'),
	(42, 'Aрккосинус Ahrrjcbyec', ' Это обратная тригонометрическая функция', 'https://clck.ru/SHvgT'),
	(43, 'Арккосинус угла a Fhrrjcbyec eukf ф', 'Это угол 0°≤α≤180° (0≤α≤π), косинус которого равен a', 'https://clck.ru/SHvm2'),
	(44, 'Арктангенс числа a  Fhrnfyutyc xbckf ф', 'Это угол −90°<α<90° (−π/2<α<π/2), тангенс которого равен a.', 'https://clck.ru/SHwAY'),
	(45, 'Арктангенс Fhrnfyutyc', 'Это обратная тригонометрическая функция.', 'https://clck.ru/SHwMT'),
	(46, 'Аргумент Fhuevtyn ', 'Это обратная тригонометрическая функция.', 'https://clck.ru/SHwRu'),
	(47, 'Арккотангенс числа a Fhrrjnfyutyc xbckf ф', 'Это угол 0°<α<180° (0<α<π), котангенс которого равен a', 'https://clck.ru/SHwWW'),
	(48, 'Синус числового аргумента x Cbyec xbckjdjuj fhuevtynf ч', 'Синусом числа х называется число, равное синусу угла в х радианов. Косинусом числа называется число, равное косинусу угла в х радианов. Аналогично определяются и другие тригонометрические функции числового аргумента х.', 'https://clck.ru/SHwcA'),
	(49, 'Тангенсоида Nfyutycjblf', 'График функции у = tgx; плоская кривая, изображающая изменение тангенса в от изменения его аргумента (угла)', 'https://clck.ru/SHwgN'),
	(50, 'Котангенсоида Rjnfyutycjblf', 'График функции у=ctg х в прямоугольной декартовой системе координат', 'https://clck.ru/SHwmH');
/*!40000 ALTER TABLE `trigonometry` ENABLE KEYS */;

-- Дамп структуры для таблица testdb.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `first_reg` datetime DEFAULT CURRENT_TIMESTAMP,
  `rereg` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дамп данных таблицы testdb.users: ~2 rows (приблизительно)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `user_id`, `first_name`, `last_name`, `first_reg`, `rereg`) VALUES
	(1, 479358154, 'Илья', 'Герасенков', '1111-11-11 11:11:11', '1212-12-12 12:12:12'),
	(25, 739239599, 'Алексей', 'Навальный', '2020-11-28 15:40:20', NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
