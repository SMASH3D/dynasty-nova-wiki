<?php
require $argv[1] . '/vendor/autoload.php';
use App\User\Domain\ValueObject as V;
$out = ['source' => 'astro-nova-backend ' . trim(shell_exec('git -C ' . escapeshellarg($argv[1]) . ' rev-parse --short HEAD'))];
$r = new ReflectionClass(V\TalentTreeRules::class); $out['rules'] = $r->getConstants();
$r = new ReflectionClass(V\PlayerBonuses::class); $out['ceilings'] = $r->getConstants();
$out['respec'] = ['price' => V\TalentRespec::PRICE, 'cooldown_hours' => V\TalentRespec::COOLDOWN_HOURS];
$r = new ReflectionClass(V\ClassChangeAllowance::class); $out['class_change'] = $r->getConstants();
$r = new ReflectionClass(V\PlayerExperience::class); $out['experience'] = $r->getConstants();
$r = new ReflectionClass(V\DynastyTraits::class); $out['trait_constants'] = $r->getConstants();
$eff = function (V\TalentEffects $es) { $a = []; foreach ($es as $e) { $a[] = ['lever' => $e->lever->value, 'value' => $e->value, 'option' => $e->option?->value, 'per_rank' => $e->perRank, 'fixed' => $e->fixed, 'unit' => $e->unit()->value]; } return $a; };
$tree = function (V\TalentTree $t) use ($eff) {
  $b = [];
  foreach ($t->branches as $br) {
    $nodes = [];
    foreach ($t->nodes as $k) { if ($k->branch() !== $br) continue;
      $nodes[] = ['key' => $k->value, 'row' => $k->row()->value(), 'type' => $k->type()->value, 'ranks' => $k->maxRanks()->value(), 'gate' => $k->row()->requiredTreePoints()->value(), 'level' => $k->requiredLevel()?->value(), 'effects' => $eff($k->effects())]; }
    usort($nodes, fn($x, $y) => $x['row'] <=> $y['row']);
    $b[] = ['key' => $br->value, 'column' => $br->column(), 'nodes' => $nodes];
  }
  return $b;
};
$out['trees']['common'] = $tree(V\TalentTree::common());
$levers = array_map(fn($l) => $l->value, V\TalentLever::cases());
$out['lever_units'] = array_combine($levers, array_map(fn($l) => $l->unit()->value, V\TalentLever::cases()));
foreach (V\CharacterClassKey::cases() as $c) {
  $out['classes'][$c->value] = ['exclusive_to' => $c->exclusiveTo()?->value];
  $out['trees'][$c->value] = $tree(V\TalentTree::of($c));
  $caps = V\ClassCaps::of($c); $cc = [];
  foreach (V\TalentLever::cases() as $l) { $v = $caps->capOf($l); if ($v !== null) $cc[$l->value] = $v; }
  $out['class_caps'][$c->value] = $cc;
}
foreach (V\DynastyKey::cases() as $d) {
  $out['dynasties'][$d->value] = ['playable' => $d->isPlayable(), 'traits' => [], 'classes' => array_map(fn($c) => $c->value, $d->characterClasses()->toArray())];
  foreach ($d->traits() as $t) $out['dynasties'][$d->value]['traits'][$t->value] = $eff($t->effects());
}
echo json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_PRESERVE_ZERO_FRACTION);
