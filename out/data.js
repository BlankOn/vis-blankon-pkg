function getData() {
var data = {};
data["packages"] = {};
data["packages"]["i386"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 40997, 272, 3, 559],
  ["suroboyo", 43672, 316, 3, 615],
]);
data["packages"]["amd64"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 40885, 268, 3, 568],
  ["suroboyo", 43594, 317, 3, 623],
]);
data["packages"]["armel"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 39549, 211, 2, 386],
  ["suroboyo", 41829, 227, 2, 412],
]);
data["packages"]["armhf"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 38949, 202, 2, 366],
  ["suroboyo", 41325, 218, 2, 396],
]);
data["sizes"] = {};
data["sizes"]["i386"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 57473670870, 271669758, 48001320, 5976220366],
  ["suroboyo", 65400583762, 377963678, 68701424, 6772159582],
]);
data["sizes"]["amd64"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 59721350172, 279709372, 47996754, 6030772504],
  ["suroboyo", 67264930644, 427872078, 68699892, 6762182674],
]);
data["sizes"]["armel"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 50873511130, 256166482, 47708660, 5544990966],
  ["suroboyo", 55275954028, 276986454, 47708660, 6022337098],
]);
data["sizes"]["armhf"] = google.visualization.arrayToDataTable([
  ["Release", "main", "extras", "extras-restricted", "restricted"],
  ["rote", 49007978890, 236634514, 47708660, 5526866914],
  ["suroboyo", 53815909834, 257455488, 47708660, 6011862410],
]);
return data;
}
