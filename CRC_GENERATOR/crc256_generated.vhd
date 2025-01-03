-- vim: ts=4 sw=4 expandtab

-- THIS IS GENERATED VHDL CODE.
-- https://bues.ch/h/crcgen
-- 
-- This code is Public Domain.
-- Permission to use, copy, modify, and/or distribute this software for any
-- purpose with or without fee is hereby granted.
-- 
-- THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
-- WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
-- MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
-- SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
-- RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
-- NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE
-- USE OR PERFORMANCE OF THIS SOFTWARE.

-- CRC polynomial coefficients: x^256 + x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1
--                              0xEDB8832080000000000000000000000000000000000000000000000000000000 (hex)
-- CRC width:                   256 bits
-- CRC shift direction:         right (little endian)
-- Input word width:            8 bits

library IEEE;
use IEEE.std_logic_1164.all;

entity crc is
    port (
        crcIn: in std_logic_vector(255 downto 0);
        data: in std_logic_vector(7 downto 0);
        crcOut: out std_logic_vector(255 downto 0)
    );
end entity crc;

architecture Behavioral of crc is
begin
    crcOut(0) <= crcIn(8);
    crcOut(1) <= crcIn(9);
    crcOut(2) <= crcIn(10);
    crcOut(3) <= crcIn(11);
    crcOut(4) <= crcIn(12);
    crcOut(5) <= crcIn(13);
    crcOut(6) <= crcIn(14);
    crcOut(7) <= crcIn(15);
    crcOut(8) <= crcIn(16);
    crcOut(9) <= crcIn(17);
    crcOut(10) <= crcIn(18);
    crcOut(11) <= crcIn(19);
    crcOut(12) <= crcIn(20);
    crcOut(13) <= crcIn(21);
    crcOut(14) <= crcIn(22);
    crcOut(15) <= crcIn(23);
    crcOut(16) <= crcIn(24);
    crcOut(17) <= crcIn(25);
    crcOut(18) <= crcIn(26);
    crcOut(19) <= crcIn(27);
    crcOut(20) <= crcIn(28);
    crcOut(21) <= crcIn(29);
    crcOut(22) <= crcIn(30);
    crcOut(23) <= crcIn(31);
    crcOut(24) <= crcIn(32);
    crcOut(25) <= crcIn(33);
    crcOut(26) <= crcIn(34);
    crcOut(27) <= crcIn(35);
    crcOut(28) <= crcIn(36);
    crcOut(29) <= crcIn(37);
    crcOut(30) <= crcIn(38);
    crcOut(31) <= crcIn(39);
    crcOut(32) <= crcIn(40);
    crcOut(33) <= crcIn(41);
    crcOut(34) <= crcIn(42);
    crcOut(35) <= crcIn(43);
    crcOut(36) <= crcIn(44);
    crcOut(37) <= crcIn(45);
    crcOut(38) <= crcIn(46);
    crcOut(39) <= crcIn(47);
    crcOut(40) <= crcIn(48);
    crcOut(41) <= crcIn(49);
    crcOut(42) <= crcIn(50);
    crcOut(43) <= crcIn(51);
    crcOut(44) <= crcIn(52);
    crcOut(45) <= crcIn(53);
    crcOut(46) <= crcIn(54);
    crcOut(47) <= crcIn(55);
    crcOut(48) <= crcIn(56);
    crcOut(49) <= crcIn(57);
    crcOut(50) <= crcIn(58);
    crcOut(51) <= crcIn(59);
    crcOut(52) <= crcIn(60);
    crcOut(53) <= crcIn(61);
    crcOut(54) <= crcIn(62);
    crcOut(55) <= crcIn(63);
    crcOut(56) <= crcIn(64);
    crcOut(57) <= crcIn(65);
    crcOut(58) <= crcIn(66);
    crcOut(59) <= crcIn(67);
    crcOut(60) <= crcIn(68);
    crcOut(61) <= crcIn(69);
    crcOut(62) <= crcIn(70);
    crcOut(63) <= crcIn(71);
    crcOut(64) <= crcIn(72);
    crcOut(65) <= crcIn(73);
    crcOut(66) <= crcIn(74);
    crcOut(67) <= crcIn(75);
    crcOut(68) <= crcIn(76);
    crcOut(69) <= crcIn(77);
    crcOut(70) <= crcIn(78);
    crcOut(71) <= crcIn(79);
    crcOut(72) <= crcIn(80);
    crcOut(73) <= crcIn(81);
    crcOut(74) <= crcIn(82);
    crcOut(75) <= crcIn(83);
    crcOut(76) <= crcIn(84);
    crcOut(77) <= crcIn(85);
    crcOut(78) <= crcIn(86);
    crcOut(79) <= crcIn(87);
    crcOut(80) <= crcIn(88);
    crcOut(81) <= crcIn(89);
    crcOut(82) <= crcIn(90);
    crcOut(83) <= crcIn(91);
    crcOut(84) <= crcIn(92);
    crcOut(85) <= crcIn(93);
    crcOut(86) <= crcIn(94);
    crcOut(87) <= crcIn(95);
    crcOut(88) <= crcIn(96);
    crcOut(89) <= crcIn(97);
    crcOut(90) <= crcIn(98);
    crcOut(91) <= crcIn(99);
    crcOut(92) <= crcIn(100);
    crcOut(93) <= crcIn(101);
    crcOut(94) <= crcIn(102);
    crcOut(95) <= crcIn(103);
    crcOut(96) <= crcIn(104);
    crcOut(97) <= crcIn(105);
    crcOut(98) <= crcIn(106);
    crcOut(99) <= crcIn(107);
    crcOut(100) <= crcIn(108);
    crcOut(101) <= crcIn(109);
    crcOut(102) <= crcIn(110);
    crcOut(103) <= crcIn(111);
    crcOut(104) <= crcIn(112);
    crcOut(105) <= crcIn(113);
    crcOut(106) <= crcIn(114);
    crcOut(107) <= crcIn(115);
    crcOut(108) <= crcIn(116);
    crcOut(109) <= crcIn(117);
    crcOut(110) <= crcIn(118);
    crcOut(111) <= crcIn(119);
    crcOut(112) <= crcIn(120);
    crcOut(113) <= crcIn(121);
    crcOut(114) <= crcIn(122);
    crcOut(115) <= crcIn(123);
    crcOut(116) <= crcIn(124);
    crcOut(117) <= crcIn(125);
    crcOut(118) <= crcIn(126);
    crcOut(119) <= crcIn(127);
    crcOut(120) <= crcIn(128);
    crcOut(121) <= crcIn(129);
    crcOut(122) <= crcIn(130);
    crcOut(123) <= crcIn(131);
    crcOut(124) <= crcIn(132);
    crcOut(125) <= crcIn(133);
    crcOut(126) <= crcIn(134);
    crcOut(127) <= crcIn(135);
    crcOut(128) <= crcIn(136);
    crcOut(129) <= crcIn(137);
    crcOut(130) <= crcIn(138);
    crcOut(131) <= crcIn(139);
    crcOut(132) <= crcIn(140);
    crcOut(133) <= crcIn(141);
    crcOut(134) <= crcIn(142);
    crcOut(135) <= crcIn(143);
    crcOut(136) <= crcIn(144);
    crcOut(137) <= crcIn(145);
    crcOut(138) <= crcIn(146);
    crcOut(139) <= crcIn(147);
    crcOut(140) <= crcIn(148);
    crcOut(141) <= crcIn(149);
    crcOut(142) <= crcIn(150);
    crcOut(143) <= crcIn(151);
    crcOut(144) <= crcIn(152);
    crcOut(145) <= crcIn(153);
    crcOut(146) <= crcIn(154);
    crcOut(147) <= crcIn(155);
    crcOut(148) <= crcIn(156);
    crcOut(149) <= crcIn(157);
    crcOut(150) <= crcIn(158);
    crcOut(151) <= crcIn(159);
    crcOut(152) <= crcIn(160);
    crcOut(153) <= crcIn(161);
    crcOut(154) <= crcIn(162);
    crcOut(155) <= crcIn(163);
    crcOut(156) <= crcIn(164);
    crcOut(157) <= crcIn(165);
    crcOut(158) <= crcIn(166);
    crcOut(159) <= crcIn(167);
    crcOut(160) <= crcIn(168);
    crcOut(161) <= crcIn(169);
    crcOut(162) <= crcIn(170);
    crcOut(163) <= crcIn(171);
    crcOut(164) <= crcIn(172);
    crcOut(165) <= crcIn(173);
    crcOut(166) <= crcIn(174);
    crcOut(167) <= crcIn(175);
    crcOut(168) <= crcIn(176);
    crcOut(169) <= crcIn(177);
    crcOut(170) <= crcIn(178);
    crcOut(171) <= crcIn(179);
    crcOut(172) <= crcIn(180);
    crcOut(173) <= crcIn(181);
    crcOut(174) <= crcIn(182);
    crcOut(175) <= crcIn(183);
    crcOut(176) <= crcIn(184);
    crcOut(177) <= crcIn(185);
    crcOut(178) <= crcIn(186);
    crcOut(179) <= crcIn(187);
    crcOut(180) <= crcIn(188);
    crcOut(181) <= crcIn(189);
    crcOut(182) <= crcIn(190);
    crcOut(183) <= crcIn(191);
    crcOut(184) <= crcIn(192);
    crcOut(185) <= crcIn(193);
    crcOut(186) <= crcIn(194);
    crcOut(187) <= crcIn(195);
    crcOut(188) <= crcIn(196);
    crcOut(189) <= crcIn(197);
    crcOut(190) <= crcIn(198);
    crcOut(191) <= crcIn(199);
    crcOut(192) <= crcIn(200);
    crcOut(193) <= crcIn(201);
    crcOut(194) <= crcIn(202);
    crcOut(195) <= crcIn(203);
    crcOut(196) <= crcIn(204);
    crcOut(197) <= crcIn(205);
    crcOut(198) <= crcIn(206);
    crcOut(199) <= crcIn(207);
    crcOut(200) <= crcIn(208);
    crcOut(201) <= crcIn(209);
    crcOut(202) <= crcIn(210);
    crcOut(203) <= crcIn(211);
    crcOut(204) <= crcIn(212);
    crcOut(205) <= crcIn(213);
    crcOut(206) <= crcIn(214);
    crcOut(207) <= crcIn(215);
    crcOut(208) <= crcIn(216);
    crcOut(209) <= crcIn(217);
    crcOut(210) <= crcIn(218);
    crcOut(211) <= crcIn(219);
    crcOut(212) <= crcIn(220);
    crcOut(213) <= crcIn(221);
    crcOut(214) <= crcIn(222);
    crcOut(215) <= crcIn(223);
    crcOut(216) <= crcIn(0) xor crcIn(224) xor data(0);
    crcOut(217) <= crcIn(1) xor crcIn(225) xor data(1);
    crcOut(218) <= crcIn(2) xor crcIn(226) xor data(2);
    crcOut(219) <= crcIn(3) xor crcIn(227) xor data(3);
    crcOut(220) <= crcIn(4) xor crcIn(228) xor data(4);
    crcOut(221) <= crcIn(5) xor crcIn(229) xor data(5);
    crcOut(222) <= crcIn(0) xor crcIn(6) xor crcIn(230) xor data(0) xor data(6);
    crcOut(223) <= crcIn(1) xor crcIn(7) xor crcIn(231) xor data(1) xor data(7);
    crcOut(224) <= crcIn(2) xor crcIn(232) xor data(2);
    crcOut(225) <= crcIn(0) xor crcIn(3) xor crcIn(233) xor data(0) xor data(3);
    crcOut(226) <= crcIn(0) xor crcIn(1) xor crcIn(4) xor crcIn(234) xor data(0) xor data(1) xor data(4);
    crcOut(227) <= crcIn(1) xor crcIn(2) xor crcIn(5) xor crcIn(235) xor data(1) xor data(2) xor data(5);
    crcOut(228) <= crcIn(2) xor crcIn(3) xor crcIn(6) xor crcIn(236) xor data(2) xor data(3) xor data(6);
    crcOut(229) <= crcIn(3) xor crcIn(4) xor crcIn(7) xor crcIn(237) xor data(3) xor data(4) xor data(7);
    crcOut(230) <= crcIn(4) xor crcIn(5) xor crcIn(238) xor data(4) xor data(5);
    crcOut(231) <= crcIn(5) xor crcIn(6) xor crcIn(239) xor data(5) xor data(6);
    crcOut(232) <= crcIn(0) xor crcIn(6) xor crcIn(7) xor crcIn(240) xor data(0) xor data(6) xor data(7);
    crcOut(233) <= crcIn(1) xor crcIn(7) xor crcIn(241) xor data(1) xor data(7);
    crcOut(234) <= crcIn(2) xor crcIn(242) xor data(2);
    crcOut(235) <= crcIn(3) xor crcIn(243) xor data(3);
    crcOut(236) <= crcIn(0) xor crcIn(4) xor crcIn(244) xor data(0) xor data(4);
    crcOut(237) <= crcIn(0) xor crcIn(1) xor crcIn(5) xor crcIn(245) xor data(0) xor data(1) xor data(5);
    crcOut(238) <= crcIn(0) xor crcIn(1) xor crcIn(2) xor crcIn(6) xor crcIn(246) xor data(0) xor data(1) xor data(2) xor data(6);
    crcOut(239) <= crcIn(1) xor crcIn(2) xor crcIn(3) xor crcIn(7) xor crcIn(247) xor data(1) xor data(2) xor data(3) xor data(7);
    crcOut(240) <= crcIn(0) xor crcIn(2) xor crcIn(3) xor crcIn(4) xor crcIn(248) xor data(0) xor data(2) xor data(3) xor data(4);
    crcOut(241) <= crcIn(0) xor crcIn(1) xor crcIn(3) xor crcIn(4) xor crcIn(5) xor crcIn(249) xor data(0) xor data(1) xor data(3) xor data(4) xor data(5);
    crcOut(242) <= crcIn(1) xor crcIn(2) xor crcIn(4) xor crcIn(5) xor crcIn(6) xor crcIn(250) xor data(1) xor data(2) xor data(4) xor data(5) xor data(6);
    crcOut(243) <= crcIn(0) xor crcIn(2) xor crcIn(3) xor crcIn(5) xor crcIn(6) xor crcIn(7) xor crcIn(251) xor data(0) xor data(2) xor data(3) xor data(5) xor data(6) xor data(7);
    crcOut(244) <= crcIn(0) xor crcIn(1) xor crcIn(3) xor crcIn(4) xor crcIn(6) xor crcIn(7) xor crcIn(252) xor data(0) xor data(1) xor data(3) xor data(4) xor data(6) xor data(7);
    crcOut(245) <= crcIn(1) xor crcIn(2) xor crcIn(4) xor crcIn(5) xor crcIn(7) xor crcIn(253) xor data(1) xor data(2) xor data(4) xor data(5) xor data(7);
    crcOut(246) <= crcIn(0) xor crcIn(2) xor crcIn(3) xor crcIn(5) xor crcIn(6) xor crcIn(254) xor data(0) xor data(2) xor data(3) xor data(5) xor data(6);
    crcOut(247) <= crcIn(0) xor crcIn(1) xor crcIn(3) xor crcIn(4) xor crcIn(6) xor crcIn(7) xor crcIn(255) xor data(0) xor data(1) xor data(3) xor data(4) xor data(6) xor data(7);
    crcOut(248) <= crcIn(0) xor crcIn(1) xor crcIn(2) xor crcIn(4) xor crcIn(5) xor crcIn(7) xor data(0) xor data(1) xor data(2) xor data(4) xor data(5) xor data(7);
    crcOut(249) <= crcIn(1) xor crcIn(2) xor crcIn(3) xor crcIn(5) xor crcIn(6) xor data(1) xor data(2) xor data(3) xor data(5) xor data(6);
    crcOut(250) <= crcIn(2) xor crcIn(3) xor crcIn(4) xor crcIn(6) xor crcIn(7) xor data(2) xor data(3) xor data(4) xor data(6) xor data(7);
    crcOut(251) <= crcIn(3) xor crcIn(4) xor crcIn(5) xor crcIn(7) xor data(3) xor data(4) xor data(5) xor data(7);
    crcOut(252) <= crcIn(4) xor crcIn(5) xor crcIn(6) xor data(4) xor data(5) xor data(6);
    crcOut(253) <= crcIn(5) xor crcIn(6) xor crcIn(7) xor data(5) xor data(6) xor data(7);
    crcOut(254) <= crcIn(6) xor crcIn(7) xor data(6) xor data(7);
    crcOut(255) <= crcIn(7) xor data(7);
end architecture Behavioral;
