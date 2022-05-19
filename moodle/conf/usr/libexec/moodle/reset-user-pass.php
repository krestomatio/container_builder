<?php
// description: reset a user password, using a hash compatible with bcrypt.

define('CLI_SCRIPT', true);

$MOODLE_APP = getenv('MOODLE_APP') ?: '/var/www/html';
require($MOODLE_APP . '/config.php');
require_once($CFG->libdir.'/clilib.php');

list($options, $unrecognized) = cli_get_params([
    'help'    => false,
    'userid' => false,
    'hash' => false,
], [
    'i' => 'userid',
    'h' => 'hash'
]);

if ($unrecognized) {
    $unrecognized = implode(PHP_EOL.'  ', $unrecognized);
    cli_error(get_string('cliunknowoption', 'core_admin', $unrecognized));
}

if ($options['help']) {
    cli_writeln("Reset a user password hash. It should be compatible with bcrypt.
Options:
        --help               Print out this help
    -i, --userid=2           User id in the database
    -h, --hash=<hash>        BCrypt compatible hash of the user password
Example:
\$ php /usr/libexec/moodle/reset-user-pass.php --userid=2 --hash='\$2b\$10\$zbRuwPil1wNWQUkvlkchwe3/rOljJvoheydndKH1X0bdIIigy0xim'");
    exit(2);
}

// vars
$userid=$options['userid'];
$hash=$options['hash'];

// verify
if(empty($userid)){
    cli_error("Please provide a user id");
}

if(empty($hash)){
    cli_error("Please provide a compatible BCrypt hash");
}

if( strlen($hash) != 60 || !preg_match('/^\$2[ayb]\$.{56}$/', $hash ) ){
    cli_error("Provided hash does not comply with format");
}

// check user id exists.
if (!$user = $DB->get_record('user', array('auth'=>'manual', 'id'=>$userid, 'mnethostid'=>$CFG->mnet_localhost_id))) {
    cli_error("Can not find user '$userid'");
}

$DB->set_field('user', 'password', $hash, array('id'=>$user->id));

echo "Password changed\n";
?>
